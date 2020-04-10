* replace the path below by the path to the folder in which you put the data files
cd "D:\_sss\_RPs\20_ Bessembinder & Lemmon\_WP1"


* unzip the file and load the file and delete the file
local dataf "data_multi_auction_2019-04-16T20_26_11.178879_anonimized"
cap unzipfile "`dataf'.zip"
import delimited "`dataf'.csv", bindquote(strict)  clear
rm "`dataf'.csv"


********************************************************
********************************************************
* make booleans of true/false
sort au_id
tostring au_id, generate(au_id_st)
encode au_id_st, generate(au_id2)
gen of_cleared2 = (of_cleared=="True")
drop of_cleared
rename of_cleared2 of_cleared
// summarize of_cleared

gen pl_testing_finished2 = (pl_testing_finished=="True")
drop pl_testing_finished
rename pl_testing_finished2 pl_testing_finished

gen pl_male2 = (pl_male=="True")
drop pl_male
rename pl_male2 pl_male

gen of_updated2 = (of_updated=="True")
drop of_updated
rename of_updated2 of_updated

gen of_canceled2 = (of_canceled=="True")
drop of_canceled
rename of_canceled2 of_canceled

gen au_is_part_experiment2 = (au_is_part_experiment=="True") & (au_id<4700000|au_id==4703335 )& au_id!=1499888 & tr_idd<4
// gen au_is_part_experiment2 = (au_is_part_experiment=="True") if tr_idd<4
drop au_is_part_experiment
rename au_is_part_experiment2 au_is_part_experiment
compress *
********************************************************
********************************************************

cap egen byte tag_per_auction = tag(au_id) if au_is_part_experiment==1


* label treatment variables
gen tr_sorted= round(tr_idd)
recode  tr_sorted (1=3) (2=1) (3=2) (5/55=.)
label variable tr_sorted "Treatment"
cap label define tr_sorted_lab 3 "20-100" 2 "40-80" 1 "55-65"
label values tr_sorted tr_sorted_lab
cap label define tr_sorted_lab2 1 "T1: 55-65" 2 "T2: 40-80" 3 "T3: 20-100" 
label values tr_sorted tr_sorted_lab2


********************************************************
* these are the independent groups
bysort gr_id :summ gr_id
bysort gr_id :summ gr_id if au_is_part_experiment==1
egen byte tag_per_group = tag(au_id gr_id) if au_is_part_experiment==1
egen byte tag_per_player_period = tag(pl_id ps_period) if au_is_part_experiment==1

********************************************************
*make unique identifyers for groups
gen au_gr_id = int(au_id2) *1000 + gr_id*100  if au_is_part_experiment==1
gen au_gr_id5 = int(au_id2) *1000 + gr_id*100  if au_is_part_experiment==1 & ps_period>5
gen au_gr_pe_id = int(au_id2) *1000 + gr_id*100 + ps_period if au_is_part_experiment==1
gen au_gr_pe_id5 = int(au_id2) *1000 + gr_id*100 + ps_period if au_is_part_experiment==1 & ps_period>5

sort au_id2 gr_id ps_period pl_id
cap drop tr_au_gr
gen tr_au_gr = int(tr_sorted)*1000 + au_id2*10+ gr_id if au_is_part_experiment==1
egen byte tag_tr_au_gr = tag(tr_au_gr ) if au_is_part_experiment==1
egen byte tag_per_auction_gr_pe_ph = tag(au_gr_pe_id) if of_offer_tiepe==0 & of_cleared==1  & ph_idd==1 & au_is_part_experiment==1
egen byte tag_per_auction_gr_pe_ph5 = tag(au_gr_pe_id) if of_offer_tiepe==0 & of_cleared==1  & ph_idd==1 & au_is_part_experiment==1 & ps_period>5
egen byte tag_per_auction_gr_ph = tag(au_gr_id) if of_offer_tiepe==0 & of_cleared==1  & ph_idd==1  & au_is_part_experiment==1
egen byte tag_per_auction_gr_ph5 = tag(au_gr_id) if of_offer_tiepe==0 & of_cleared==1  & ph_idd==1  & au_is_part_experiment==1 & ps_period>5
egen byte tag_per_auction_gr = tag(au_gr_id) if au_is_part_experiment==1
egen byte tag_per_auction_gr5 = tag(au_gr_id5) if au_is_part_experiment==1 & ps_period>5 & of_cleared==1 & of_offer_tiepe==0 
gen tr_pe_id = int(tr_sorted) *1000 + ps_period
egen byte tag_per_tr_pe = tag(tr_pe_id ) if au_is_part_experiment==1
cap egen byte tag_per_player = tag(pl_id) if au_is_part_experiment==1

tab tr_sorted tag_per_auction_gr_pe_ph 
list au_gr_id if tag_per_auction_gr_ph==1 & tr_sorted==2


********************************************************
* What are the forward positions?

*	ra=0.05				ra=0.005
*   20-100:	16.2561		20-100:	16.2561
* 	40-80: 	15.0005		40-80: 	15.0005
* 	55-65:	-14.6296	55-65:	14.6296



********************************************************
********************************************************
*calculate the weighted mean of prices - cannot take simply mean, because it must be weighted by the number of units traded for that price!

* total_expense_transaction per cleared offer (thus per transaction)
* Note: both buyer and seller are recorded, so every transaction shows up TWICE.
* Therefore, only take the one of the seller: of_offer_tiepe==0
gen tot_expense_transaction = of_pricecleared * of_unitscleared if of_cleared==1 & of_offer_tiepe==0 & au_is_part_experiment==1
gen tot_expense_transaction5 = of_pricecleared * of_unitscleared if of_cleared==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1
* already exists as of_product... check if the same... OK
summ tot_expense_transaction of_product if of_cleared==1 & of_offer_tiepe==0 & au_is_part_experiment==1


* total_expense_transaction per auction, group, period, and phase (thus total expense within a phase)
by ps_auction ps_group ps_period ph_idd, sort : egen float tot_expense_a_gr_pe_ph = total(tot_expense_transaction) if of_cleared==1 & of_offer_tiepe==0 & au_is_part_experiment==1
by ps_auction ps_group ps_period ph_idd, sort : egen float tot_expense_a_gr_pe5_ph = total(tot_expense_transaction) if of_cleared==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1

label variable tot_expense_a_gr_pe_ph "total_expense_auction_group_period_phase"
label variable tot_expense_a_gr_pe5_ph "total_expense_auction_group_period5_phase"

* total_unitscleared per auction, group, period, and phase (thus total units traded within a phase)
by ps_auction ps_group ps_period ph_idd, sort : egen float tot_unitscleared_a_gr_pe_ph = total(of_unitscleared) if of_cleared==1 & of_offer_tiepe==0 & au_is_part_experiment==1
by ps_auction ps_group ps_period ph_idd, sort : egen float tot_unitscleared_a_gr_pe5_ph = total(of_unitscleared) if of_cleared==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1
label variable tot_unitscleared_a_gr_pe_ph "total_unitscleared_group_auction_period_phase"
label variable tot_unitscleared_a_gr_pe5_ph "total_unitscleared_group_auction_period5_phase"

* weighted mean price per auction, group, and period (thus average within a phase)
by ps_auction ps_period ph_idd, sort : gen wmean_price_a_gr_pe_ph = tot_expense_a_gr_pe_ph /tot_unitscleared_a_gr_pe_ph if  of_offer_tiepe==0 & au_is_part_experiment==1
by ps_auction ps_period ph_idd, sort : gen wmean_price_a_gr_pe5_ph = tot_expense_a_gr_pe5_ph /tot_unitscleared_a_gr_pe5_ph if  of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1
label variable wmean_price_a_gr_pe_ph "wmean_price_auction_group_period_phase"
label variable wmean_price_a_gr_pe5_ph "wmean_price_auction_group_period5_phase"

* show the weighted mean price per auction, group, period in phase 1 (forward market)
sort ps_auction ps_group ps_period ph_idd
by ps_auction ps_group ps_period, sort : summ wmean_price_a_gr_pe_ph if ph_idd==1 & of_offer_tiepe==0 & au_is_part_experiment==1
by ps_auction ps_group ps_period, sort : summ wmean_price_a_gr_pe5_ph if ph_idd==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1

* forward premium (absolute) per auction, group and period
gen float fpremium_a_gr_pe = wmean_price_a_gr_pe_ph  - tr_price_avg_theory if of_cleared==1 & ph_idd==1 & of_offer_tiepe==0 & au_is_part_experiment==1
gen float fpremium_a_gr_pe5 = wmean_price_a_gr_pe_ph  - tr_price_avg_theory if of_cleared==1 & ph_idd==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1
label variable fpremium_a_gr_pe "fpremium_auction_group_period"
label variable fpremium_a_gr_pe5 "fpremium_auction_group_period5"

* forward premium (relative) per auction, group and period (averaged withing phase 1 (forward market))
gen float fpremium_rel_a_gr_pe = (wmean_price_a_gr_pe_ph  - tr_price_avg_theory)/tr_price_avg_theory  if of_cleared==1 & ph_idd==1 & of_offer_tiepe==0 & au_is_part_experiment==1
gen float fpremium_rel_a_gr_pe5 = (wmean_price_a_gr_pe_ph  - tr_price_avg_theory)/tr_price_avg_theory  if of_cleared==1 & ph_idd==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1
label variable fpremium_rel_a_gr_pe "fpremium_relative_auction_group_period"
label variable fpremium_rel_a_gr_pe5 "fpremium_relative_auction_group_period5"

by ps_auction ps_group  ps_period , sort : summ fpremium_a_gr_pe if ph_idd==1 & of_offer_tiepe==0 & au_is_part_experiment==1
by ps_auction ps_group  ps_period , sort : summ fpremium_a_gr_pe5 if ph_idd==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1
by ps_auction ps_group ps_period , sort : summ fpremium_rel_a_gr_pe if ph_idd==1 & of_offer_tiepe==0 & au_is_part_experiment==1
by ps_auction ps_group ps_period , sort : summ fpremium_rel_a_gr_pe5 if ph_idd==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1

// cap drop p_compPrice
gen tp_compPrice = ps_player_demand
recode tp_compPrice (1=0) (2=0.1) (3=0.3) (4=0.7) (5=1.7) (6=3) (7=4.9) (8=7.5) (9=11) (10=14.8) (11=21) (12=27) (13=35) (14=44) (15=54) (16=66) (17=80) (18=94) (19=115) (20=130) (21=155) (22=175) (23=205) (24=230) (25=260) (26/44=9999), gen(p_compPrice)
drop tp_compPrice 

* forward premium (absolute) per auction and group (averaged over all periods within a group)
by ps_auction ps_group, sort : egen float fpremium_a_gr = mean(fpremium_a_gr_pe) if of_cleared==1 & of_offer_tiepe==0 & au_is_part_experiment==1
by ps_auction ps_group, sort : egen float fpremium_a_gr5 = mean(fpremium_a_gr_pe5) if of_cleared==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1
label variable fpremium_a_gr "fpremium_auction_group"
label variable fpremium_a_gr5 "fpremium_auction_group5"
label variable ps_period "period"

* forward premium (relative) per auction and group (averaged over all periods within a 
* group)
by ps_auction ps_group, sort : egen float fpremium_rel_a_gr = mean(fpremium_rel_a_gr_pe) if of_cleared==1 & of_offer_tiepe==0 & au_is_part_experiment==1
by ps_auction ps_group, sort : egen float fpremium_rel_a_gr5 = mean(fpremium_rel_a_gr_pe5) if of_cleared==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1
tab tr_sorted fpremium_rel_a_gr5
tab tr_sorted fpremium_rel_a_gr5 if  tag_per_auction_gr5==1 
label variable fpremium_rel_a_gr "fpremium_relative_auction_group"
label variable fpremium_rel_a_gr5 "fpremium_relative_auction_group5"

* forward premium (relative) per period and treatment (averaged over all groups )
by tr_sorted ps_period, sort : egen float fpremium_rel_a_pe_tr = mean(fpremium_rel_a_gr_pe) if of_cleared==1 & of_offer_tiepe==0 &tag_per_auction_gr_pe_ph==1 & au_is_part_experiment==1
label variable fpremium_rel_a_pe_tr "fpremium_relative_period_tr"
label variable fpremium_rel_a_gr5 "fpremium_relative_auction_group5"

*** averaged over treatment for abs
* forward premium (absolute) per treatment (averaged over all auctions, groups and periods within a treatment)
by tr_idd, sort : egen float fpremium_tr = mean(fpremium_a_gr) if of_cleared==1 & of_offer_tiepe==0 & au_is_part_experiment==1
by tr_idd, sort : egen float fpremium_tr5 = mean(fpremium_a_gr5) if of_cleared==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1
label variable fpremium_tr "fpremium_treatment"
label variable fpremium_tr5 "fpremium_treatment5"

* forward premium (relative) per treatment (averaged over all auctions, groups and periods within a treatment)
by tr_idd, sort : egen float fpremium_rel_tr = mean(fpremium_rel_a_gr) if of_cleared==1 & of_offer_tiepe==0 & au_is_part_experiment==1
by tr_idd, sort : egen float fpremium_rel_tr5 = mean(fpremium_rel_a_gr5) if of_cleared==1 & of_offer_tiepe==0 & ps_period > 5 & au_is_part_experiment==1
label variable fpremium_rel_tr "fpremium_relative_treatment"
label variable fpremium_rel_tr5 "fpremium_relative_treatment5"
label var fpremium_rel_tr "Forward Premium (av over Tr)"
label var fpremium_rel_tr5 "Forward Premium (last 5)"
label var fpremium_rel_a_gr "Forward Premium (session)"

// cap drop pl_testing_errors_av 
by ps_auction ps_group, sort: egen float pl_testing_errors_av = mean(pl_testing_errors/19)  if au_is_part_experiment==1
gen pl_testing_errors_av_neg = 1- pl_testing_errors_av
tab pl_testing_errors_av 

gen tr1= tr_sorted==1
gen tr2= tr_sorted==2
gen tr3= tr_sorted==3
label var tr1 "T1: 55-65"
label var tr2 "T2: 40-80" 
label var tr3 "T3: 20-100" 

tab tr1 if tag_per_auction==1
tab tr2 if tag_per_auction==1
tab tr3 if tag_per_auction==1
sort au_id 
// list au_id if tag_per_auction==1 & tr2==1

by au_gr_id, sort : egen float testing_errors_max_gr = max(pl_testing_errors) if au_is_part_experiment==1

// tab au_gr_id tag_per_auction_gr_pe_ph if tr_idd<5
// tab au_gr_pe_id tag_per_auction_gr_pe_ph if tr_sorted< 4 &tr_idd<5
// tab fpremium_rel_a_gr_pe tag_per_auction_gr_pe_ph if tr_sorted< 4 &tr_idd<5
// tab au_gr_pe_id tag_per_auction_gr_pe_ph if tr_sorted< 4 &tr_idd<5

by tr_sorted, sort: tab au_gr_pe_id tag_per_auction_gr_pe_ph if tr_sorted< 4 &tr_idd<5

cap drop tr3_vs_tr1
cap drop tr3_vs_tr2
cap drop tr2_vs_tr1
gen tr3_vs_tr1 = tr_sorted==3 if (tr_sorted==1|tr_sorted==3) &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
summ tr3_vs_tr1 
gen tr3_vs_tr2 = tr_sorted==3 if (tr_sorted==2|tr_sorted==3) &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
gen tr2_vs_tr1 = tr_sorted==2 if (tr_sorted==2|tr_sorted==1) &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1 
tab tr2_vs_tr1
label var fpremium_rel_a_gr_pe "fpremium (averaged within a round for a group)"


gen tr3_vs_tr1_5 = tr_sorted==3 if (tr_sorted==1|tr_sorted==3) &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
summ tr3_vs_tr1 if au_is_part_experiment==1
summ tr3_vs_tr2
summ tr2_vs_tr1  
gen tr3_vs_tr2_5 = tr_sorted==3 if (tr_sorted==2|tr_sorted==3) &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
gen tr2_vs_tr1_5 = tr_sorted==2 if (tr_sorted==2|tr_sorted==1) &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1 


cap drop fpremium_rel_a_gr_tr1 
cap drop fpremium_rel_a_gr_tr2 
cap drop fpremium_rel_a_gr_tr3
gen fpremium_rel_a_gr_tr1 = fpremium_rel_a_gr if tr_sorted==1 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
gen fpremium_rel_a_gr_tr2 = fpremium_rel_a_gr if tr_sorted==2 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
gen fpremium_rel_a_gr_tr3 = fpremium_rel_a_gr if tr_sorted==3 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1

gen fpremium_rel_a_gr5_tr1 = fpremium_rel_a_gr5 if tr_sorted==1 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
gen fpremium_rel_a_gr5_tr2 = fpremium_rel_a_gr5 if tr_sorted==2 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
gen fpremium_rel_a_gr5_tr3 = fpremium_rel_a_gr5 if tr_sorted==3 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1 


*********************************************************
* create vars for 95% area fpremium
cap drop fpremium_rel_a_gr_pe_mean 
egen float fpremium_rel_a_gr_pe_mean = mean(fpremium_rel_a_gr_pe) if tag_per_auction_gr_pe_ph==1 & au_is_part_experiment==1, by (tr_sorted ps_period)
egen float fpremium_rel_a_gr_pe_sd = sd(fpremium_rel_a_gr_pe) if tag_per_auction_gr_pe_ph==1 & au_is_part_experiment==1, by (tr_sorted ps_period)
egen float fpremium_rel_a_gr_pe_n = count(fpremium_rel_a_gr_pe) if tag_per_auction_gr_pe_ph==1 & au_is_part_experiment==1, by (tr_sorted ps_period)
bysort tr_sorted ps_period:gen fpremium_rel_a_gr_pe_se  = fpremium_rel_a_gr_pe_sd/sqrt(fpremium_rel_a_gr_pe_n) if tag_per_auction_gr_pe_ph==1 & au_is_part_experiment==1
bysort tr_sorted ps_period:gen fpremium_rel_a_gr_pe_ub95  = fpremium_rel_a_gr_pe_mean + 1.96* fpremium_rel_a_gr_pe_se if tag_per_auction_gr_pe_ph==1 & au_is_part_experiment==1
bysort tr_sorted ps_period:gen fpremium_rel_a_gr_pe_lb95  = fpremium_rel_a_gr_pe_mean - 1.96* fpremium_rel_a_gr_pe_se if tag_per_auction_gr_pe_ph==1 & au_is_part_experiment==1

* check
bysort tr_sorted:tab fpremium_rel_a_gr_pe_mean ps_period 
bysort tr_sorted:tab fpremium_rel_a_gr_pe_mean ps_period 
bysort tr_sorted:tab fpremium_rel_a_gr_pe_sd  ps_period 
bysort tr_sorted:tab fpremium_rel_a_gr_pe_se  ps_period  

* create vars for bar fpremium
egen float fpremium_rel_a_gr_mean = mean(fpremium_rel_a_gr) if tag_per_auction_gr_ph==1 & au_is_part_experiment==1, by (tr_sorted)
egen float fpremium_rel_a_gr_sd = sd(fpremium_rel_a_gr) if tag_per_auction_gr_ph==1& au_is_part_experiment==1, by (tr_sorted )
egen float fpremium_rel_a_gr_n = count(fpremium_rel_a_gr) if tag_per_auction_gr_ph==1& au_is_part_experiment==1, by (tr_sorted )
bysort tr_sorted :gen fpremium_rel_a_gr_se  = fpremium_rel_a_gr_sd/sqrt(fpremium_rel_a_gr_n) if tag_per_auction_gr_ph==1& au_is_part_experiment==1
bysort tr_sorted :gen fpremium_rel_a_gr_ub95  = fpremium_rel_a_gr_mean + 1.96* fpremium_rel_a_gr_se if tag_per_auction_gr_ph==1& au_is_part_experiment==1
bysort tr_sorted :gen fpremium_rel_a_gr_lb95  = fpremium_rel_a_gr_mean - 1.96* fpremium_rel_a_gr_se if tag_per_auction_gr_ph==1& au_is_part_experiment==1

summ fpremium_rel_a_gr_sd if tr_sorted==1
summ fpremium_rel_a_gr_se if tr_sorted==1


* create vars for bar fpremium
egen float fpremium_rel_a_gr5_mean = mean(fpremium_rel_a_gr5) if tag_per_auction_gr_ph5==1 & au_is_part_experiment==1, by (tr_sorted)
egen float fpremium_rel_a_gr5_sd = sd(fpremium_rel_a_gr5) if tag_per_auction_gr_ph5==1& au_is_part_experiment==1, by (tr_sorted )
egen float fpremium_rel_a_gr5_n = count(fpremium_rel_a_gr5) if tag_per_auction_gr_ph5==1& au_is_part_experiment==1, by (tr_sorted )
bysort tr_sorted :gen fpremium_rel_a_gr5_se  = fpremium_rel_a_gr5_sd/sqrt(fpremium_rel_a_gr5_n) if tag_per_auction_gr_ph5==1& au_is_part_experiment==1
bysort tr_sorted :gen fpremium_rel_a_gr5_ub95  = fpremium_rel_a_gr5_mean + 1.96* fpremium_rel_a_gr5_se if tag_per_auction_gr_ph5==1& au_is_part_experiment==1
bysort tr_sorted :gen fpremium_rel_a_gr5_lb95  = fpremium_rel_a_gr5_mean - 1.96* fpremium_rel_a_gr5_se if tag_per_auction_gr_ph5==1& au_is_part_experiment==1

summ fpremium_rel_a_gr5 fpremium_rel_a_gr5_mean
summ fpremium_rel_a_gr5 fpremium_rel_a_gr5_mean

************************************************************************************************************************
************************************************************************************************************************
* create the fpos vars
gen fpos = ps_vouchers_used_stage1 + (-1* ps_vouchers_negative_stage1) if ph_idd==1 & tr_sorted<4
gen fpos_pred = cond(tr_sorted==1, 14.6296, cond(tr_sorted==2, 15.0005, cond(tr_sorted==3, 16.2561,.   ))) if ph_idd==1 & tr_sorted<4& au_is_part_experiment==1

egen float fpos_a_gr_pe = mean(fpos) if  au_is_part_experiment==1, by(ps_auction ps_period gr_id)
egen float fpos_a_gr_pe5 = mean(fpos) if  au_is_part_experiment==1 & ps_period>5, by(ps_auction ps_period gr_id)

// cap drop fpos_a_gr
egen float fpos_a_gr = mean(fpos) if au_is_part_experiment==1 , by(ps_auction gr_id)
egen float fpos_a_gr5 = mean(fpos) if au_is_part_experiment==1 & ps_period>5, by(ps_auction gr_id)
egen float fpos_tr = mean(fpos) if tag_per_auction_gr_pe_ph==1 & au_is_part_experiment==1, by (tr_sorted)
egen float fpos_tr5 = mean(fpos) if tag_per_auction_gr_pe_ph5==1 & au_is_part_experiment==1 & ps_period>5 , by (tr_sorted)

// egen float fpos_tr = mean(fpos_a_gr) if  tag_per_auction_gr_ph==1, by (tr_sorted)
egen float fpos_pe_tr = mean(fpos_a_gr_pe) if of_cleared==1 & of_offer_tiepe==0 &tag_per_auction_gr_pe_ph==1, by(tr_sorted ps_period)
egen float fpos_pe_tr5 = mean(fpos_a_gr_pe) if of_cleared==1 & ps_period>5 & of_offer_tiepe==0 &tag_per_auction_gr_pe_ph5==1, by(tr_sorted ps_period)
label variable fpos_pe_tr "forward position"

* create vars for area fpos
cap drop fpos_a_gr_pe_mean 
egen float fpos_a_gr_pe_mean = mean(fpos_a_gr_pe) if tag_per_auction_gr_pe_ph==1, by (tr_sorted ps_period)
// egen float fpos_a_gr_mean = mean(fpos_a_gr_pe_mean) if tag_per_auction_gr_pe_ph==1, by (tr_sorted)
egen float fpos_a_gr_pe_sd = sd(fpos_a_gr_pe) if tag_per_auction_gr_pe_ph==1, by (tr_sorted ps_period)
egen float fpos_a_gr_pe_n = count(fpos_a_gr_pe) if tag_per_auction_gr_pe_ph==1, by (tr_sorted ps_period)

egen float fpos_a_gr_pe5_mean = mean(fpos_a_gr_pe) if tag_per_auction_gr_ph5==1 & ps_period>5 , by (tr_sorted ps_period)
// egen float fpos_a_gr_mean = mean(fpos_a_gr_pe_mean) if tag_per_auction_gr_pe_ph==1, by (tr_sorted)
egen float fpos_a_gr_pe5_sd = sd(fpos_a_gr_pe) if tag_per_auction_gr_ph5==1& ps_period>5 , by (tr_sorted ps_period)
egen float fpos_a_gr_pe5_n = count(fpos_a_gr_pe) if tag_per_auction_gr_ph5==1 & ps_period>5 , by (tr_sorted ps_period)

bysort tr_sorted ps_period:gen fpos_a_gr_pe_se  = fpos_a_gr_pe_sd/sqrt(fpos_a_gr_pe_n) if tag_per_auction_gr_pe_ph==1
bysort tr_sorted ps_period:gen fpos_a_gr_pe_ub95  = fpos_a_gr_pe_mean + 1.96* fpos_a_gr_pe_se if tag_per_auction_gr_pe_ph==1
bysort tr_sorted ps_period:gen fpos_a_gr_pe_lb95  = fpos_a_gr_pe_mean - 1.96* fpos_a_gr_pe_se if tag_per_auction_gr_pe_ph==1

bysort tr_sorted ps_period:gen fpos_a_gr_pe5_se  = fpos_a_gr_pe5_sd/sqrt(fpos_a_gr_pe5_n) if tag_per_auction_gr_pe_ph5==1& ps_period>5
bysort tr_sorted ps_period:gen fpos_a_gr_pe5_ub95  = fpos_a_gr_pe5_mean + 1.96* fpos_a_gr_pe5_se if tag_per_auction_gr_pe_ph5==1& ps_period>5
bysort tr_sorted ps_period:gen fpos_a_gr_pe5_lb95  = fpos_a_gr_pe5_mean - 1.96* fpos_a_gr_pe5_se if tag_per_auction_gr_pe_ph5==1& ps_period>5

* check
bysort tr_sorted:tab fpos_a_gr_pe_mean ps_period  if tr_sorted==1
bysort tr_sorted:tab fpos_a_gr_pe_sd  ps_period 
bysort tr_sorted:tab fpos_a_gr_pe_se  ps_period  
bysort tr_sorted:tab fpos_a_gr_pe_lb95  ps_period  if tr_sorted==1 
tab fpos_a_gr_pe_mean ps_period  if tr_sorted==1
tab fpos_a_gr_pe_lb95  ps_period  if tr_sorted==1 

* create vars for bar fpos
egen float fpos_a_gr_mean = mean(fpos_a_gr) if tag_per_auction_gr_ph==1 , by (tr_sorted)
egen float fpos_a_gr_sd = sd(fpos_a_gr) if tag_per_auction_gr_ph==1, by (tr_sorted )
egen float fpos_a_gr_n = count(fpos_a_gr) if tag_per_auction_gr_ph==1, by (tr_sorted )

egen float fpos_a_gr5_mean = mean(fpos_a_gr) if tag_per_auction_gr_ph5==1 & ps_period>5, by (tr_sorted)
egen float fpos_a_gr5_sd = sd(fpos_a_gr) if tag_per_auction_gr_ph5==1& ps_period>5, by (tr_sorted )
egen float fpos_a_gr5_n = count(fpos_a_gr) if tag_per_auction_gr_ph5==1& ps_period>5, by (tr_sorted )

bysort tr_sorted :gen fpos_a_gr_se  = fpos_a_gr_sd/sqrt(fpos_a_gr_n) if tag_per_auction_gr_ph==1
bysort tr_sorted :gen fpos_a_gr_ub95  = fpos_a_gr_mean + 1.96* fpos_a_gr_se if tag_per_auction_gr_ph==1
bysort tr_sorted :gen fpos_a_gr_lb95  = fpos_a_gr_mean - 1.96* fpos_a_gr_se if tag_per_auction_gr_ph==1

bysort tr_sorted :gen fpos_a_gr5_se  = fpos_a_gr5_sd/sqrt(fpos_a_gr5_n) if tag_per_auction_gr_ph5==1 & ps_period>5
bysort tr_sorted :gen fpos_a_gr5_ub95  = fpos_a_gr5_mean + 1.96* fpos_a_gr5_se if tag_per_auction_gr_ph5==1 & ps_period>5
bysort tr_sorted :gen fpos_a_gr5_lb95  = fpos_a_gr5_mean - 1.96* fpos_a_gr5_se if tag_per_auction_gr_ph5==1 & ps_period>5
*********************************************************

egen float total_demand = total(ps_player_demand) if tag_per_player_period ==1 & tr_sorted!=. ,by(au_gr_pe_id pl_role ps_group) 
egen float total_n_per_group = count(pl_id) if tag_per_player_period ==1 & tr_sorted!=.,by(au_gr_pe_id pl_role ps_group) 
summ total_demand total_n_per_group 

egen float total_demand5 = total(ps_player_demand) if tag_per_player_period ==1 & tr_sorted!=. & ps_period>5,by(au_gr_pe_id pl_role ps_group) 
egen float total_n_per_group5 = count(pl_id) if tag_per_player_period ==1 & tr_sorted!=. & ps_period>5,by(au_gr_pe_id pl_role ps_group) 

***************************************8
* use Datasets/master
cap drop omzetByPlayerDemand meanPriceByPlayerDemand vouchersUsedInStageOne 
cap drop vouchersUsedInStageOne 
cap drop omzetByPlayerDemand 
cap drop unitsByPlayerDemand 
by ps_player_demand, sort : egen float omzetByPlayerDemand = total(of_pricecleared * of_unitscleared) if tr_sort!=. 
by ps_player_demand, sort : egen float unitsByPlayerDemand = total(of_unitscleared) if tr_sort!=.
by au_gr_id, sort : egen float vouchersUsedInStageOne =mean(ps_vouchers_used_stage1) if tr_sort!=. & pl_role==1
// by ps_player_demand, sort : egen float meanPriceByPlayerDemand = omzetByPlayerDemand / unitsByPlayerDemand 
gen meanPriceByPlayerDemand = omzetByPlayerDemand / unitsByPlayerDemand if tr_sort !=. 

gen fpos_a_gr_tr1 = fpos_a_gr if tr_sorted==1 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
gen fpos_a_gr_tr2 = fpos_a_gr if tr_sorted==2 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
gen fpos_a_gr_tr3 = fpos_a_gr if tr_sorted==3 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1

gen fpos_a_gr5_tr1 = fpos_a_gr5 if tr_sorted==1 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
gen fpos_a_gr5_tr2 = fpos_a_gr5 if tr_sorted==2 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1
gen fpos_a_gr5_tr3 = fpos_a_gr5 if tr_sorted==3 &  tag_per_auction_gr_ph5==1 & au_is_part_experiment==1

tab tr_sorted if tag_per_auction_gr==1

compress

ssc inst jonter

