********************************************************
* First run do1_ initialize_2019.11.10.do
********************************************************

************************************************************************
* Table 6: Deviation from predicted spot price
local name = "aa221.doc"

* are the spotprice differences large?
reg sprice_diff_rel_pe   ones if tag_per_auction_gr_pe_ph2==1 , noc vce(cluster au_gr_id)
outreg2 using `name' ,  label //5
reg sprice_diff_rel_pe   tr1 tr2 tr3 if tag_per_auction_gr_pe_ph2==1 , noc vce(cluster au_gr_id)
outreg2 using `name' ,  label //6
* are the spotprice differences large in the last 5 periods?
reg sprice_diff_rel_pe   ones if tag_per_auction_gr_pe_ph2==1 & ps_period>5, noc vce(cluster au_gr_id)
outreg2 using `name' ,  label //7

reg sprice_diff_rel_pe   tr1 tr2 tr3 if tag_per_auction_gr_pe_ph2==1 & ps_period>5, noc vce(cluster au_gr_id)
outreg2 using `name' ,  label //8

* F-test, parametric test * are the spotprice deviations different over treatments?
quietly reg sprice_diff_rel_pe   tr1 tr2 tr3 if tag_per_auction_gr_pe_ph2==1 , noc vce(cluster au_gr_id)
test (tr1=tr2=tr3)
quietly reg sprice_diff_rel_pe   tr1 tr2 tr3 if tag_per_auction_gr_pe_ph2==1 & ps_period>5, noc vce(cluster au_gr_id)
test (tr1=tr2=tr3)

* KW, non-parametric test * are the spotprice deviations different over treatments?
kwallis sprice_diff_rel if tag_per_auction_gr_ph==1 , by(tr_sorted)  
kwallis sprice_diff_rel5 if tag_per_auction_gr_ph5==1 , by(tr_sorted)  



************************************************************************
* Figure 4: The forward premium 
* a) By treatment and by group
twoway 	(rbar fpremium_rel_a_gr_lb95 fpremium_rel_a_gr_ub95 tr_sorted if tr_sorted==1  , sort  ///
 		 fcolor(black%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
		 (rbar fpremium_rel_a_gr_lb95 fpremium_rel_a_gr_ub95 tr_sorted if tr_sorted==2  , sort  ///
 		 fcolor(blue%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
		 (rbar fpremium_rel_a_gr_lb95 fpremium_rel_a_gr_ub95 tr_sorted if tr_sorted==3  , sort  ///
 		 fcolor(red%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
		(scatter fpremium_rel_a_gr tr_sorted if tr_sorted==1, sort ylabel(-.8(.2).4) mcolor(black)) ///
		(scatter fpremium_rel_a_gr tr_sorted if tr_sorted==2, sort ylabel(-.8(.2).4) mcolor(blue)) ///
		(scatter fpremium_rel_a_gr tr_sorted if tr_sorted==3, sort ylabel(-.8(.2).4) mcolor(red)) ///
		(scatter fpremium_rel_a_gr_mean tr_sorted if tr_sorted==1, msize(huge) mcolor(black)) ///
		(scatter fpremium_rel_a_gr_mean tr_sorted if tr_sorted==2, msize(huge) mcolor(blue)) ///
		(scatter fpremium_rel_a_gr_mean tr_sorted if tr_sorted==3, msize(huge) mcolor(red)) , ytitle(Forward Premium (%)) ///
           ytitle(, size(vlarge)) ylabel(-.8(.2).4, labsize(large)) ymtick(, labsize(large)) xtitle(, size(vlarge)) ///
		   xlabel(#3, labsize(large) valuelabel ticks) xmtick(, labsize(large) ) ///
		   legend(order(1 "groups" 4 "treatments")  cols(2)  subtitle("Averaged over:")) legend(off)

* b) By treatment and period
sort ps_period
twoway 	(rarea fpremium_rel_a_gr_pe_lb95 fpremium_rel_a_gr_pe_ub95 ps_period if tr_sorted==1 &tag_per_auction_gr_pe_ph ==1 , sort ylabel(-.8(.2).4) ///
 		 fcolor(black%20) fintensity(100) lcolor(none%50) lwidth(none)) ///
		 (rarea fpremium_rel_a_gr_pe_lb95 fpremium_rel_a_gr_pe_ub95 ps_period if tr_sorted==3 &tag_per_auction_gr_pe_ph ==1  , sort ylabel(-.8(.2).4)  ///
 		 fcolor(red%20) fintensity(100) lcolor(none%50) lwidth(none))  ///
		(line fpremium_rel_a_gr_pe_mean   ps_period if tr_sorted==1 , sort ylabel(-.8(.2).4) lcolor(black) lwidth(thick)  ytitle(Forward Premium1) ) ///
		(line fpremium_rel_a_gr_pe_mean   ps_period if tr_sorted==2 , sort ylabel(-.8(.2).4) lcolor(blue) lwidth(thick)    ytitle(Forward Premium)) ///
		(line fpremium_rel_a_gr_pe_mean    ps_period if tr_sorted==3, sort ylabel(-.8(.2).4)   lcolor(red) lwidth(thick)  ytitle(Forward Premium)) ///
		, legend(order(3 "T1: 55-65" 4 "T2: 40-80" 5 "T3: 20-100") cols(1)) xlabel(1 (1) 10)

		


************************************************************************
*** Table 7. Test results using non-parametric tests 
** Relative Forward Premium 
* Hypothesis 1
signrank fpremium_rel_a_gr_tr1 = 0
signrank fpremium_rel_a_gr_tr2 = 0
signrank fpremium_rel_a_gr_tr3 = 0

* Hypothesis 2
ranksum fpremium_rel_a_gr, by(tr2_vs_tr1)
ranksum fpremium_rel_a_gr, by(tr3_vs_tr2)
ranksum fpremium_rel_a_gr, by(tr3_vs_tr1)

** Forward Positions
* Hypothesis 3a
signrank fpos_a_gr_tr1 = 0
signrank fpos_a_gr_tr2 = 0
signrank fpos_a_gr_tr3 = 0

* Hypothesis 3b
signrank fpos_a_gr_tr1 = 14.6
signrank fpos_a_gr_tr2 = 15
signrank fpos_a_gr_tr3 = 16.3

* However, as expected, they do not differ much over the treatments. 
ranksum fpos_a_gr, by(tr2_vs_tr1)
ranksum fpos_a_gr, by(tr3_vs_tr2)
ranksum fpos_a_gr, by(tr3_vs_tr1)
jonter fpos_a_gr if  tag_per_auction_gr==1, by(tr_sorted) 



************************************************************************
* Figure 5: The forward position per treatment, predicted and observed.		
* a) By treatment and by group
twoway 	(rbar fpos_a_gr_lb95 fpos_a_gr_ub95 tr_sorted if tr_sorted==1  , sort  ///
 		 fcolor(black%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
		 (rbar fpos_a_gr_lb95 fpos_a_gr_ub95 tr_sorted if tr_sorted==2  , sort  ///
 		 fcolor(blue%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
		 (rbar fpos_a_gr_lb95 fpos_a_gr_ub95 tr_sorted if tr_sorted==3  , sort  ///
 		 fcolor(red%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
	(scatter fpos_pred  tr_sorted if tr_sorted==1, sort ylabel(-.8(.2).4) mcolor(black) lwidth(thick) lpattern(dash)  msize(vhuge) msymbol(square) ) ///
		(scatter fpos_pred  tr_sorted if tr_sorted==2, sort ylabel(-1(1)14) mcolor(blue) lwidth(thick) lpattern(dash) msize(vhuge) msymbol(square))  ///
		(scatter fpos_pred  tr_sorted if tr_sorted==3, sort ylabel(8(1)17)   mcolor(red) lwidth(thick) lpattern(dash) msize(vhuge) msymbol(square)) ///
		(scatter fpos_a_gr_mean tr_sorted if tr_sorted==1, msize(huge) mcolor(black)) ///
		(scatter fpos_a_gr_mean tr_sorted if tr_sorted==2, msize(huge) mcolor(blue)) ///
		(scatter fpos_a_gr_mean tr_sorted if tr_sorted==3, msize(huge) mcolor(red)), ytitle(Forward Position) ///
           ytitle(, size(vlarge)) ylabel(10(1)16, labsize(large)) ymtick(, labsize(large)) xtitle(, size(vlarge)) ///
		   xlabel(#3, labsize(large) valuelabel ticks) xmtick(, labsize(large) ) ///
		   legend(order(1 "groups" )  cols(2)  subtitle("Averaged over:"))	 legend(off) xscale(range(1 3.15)) 
		
* b) By treatment and period
twoway 	(rarea fpos_a_gr_pe_lb95 fpos_a_gr_pe_ub95 ps_period if tr_sorted==1  , sort ylabel(-.8(.2).4) ///
 		 fcolor(black%20) fintensity(100) lcolor(none%50) lwidth(none)) ///
		 (rarea fpos_a_gr_pe_lb95 fpos_a_gr_pe_ub95 ps_period if tr_sorted==3  , sort ylabel(-.8(.2).4) ///
 		 fcolor(red%20) fintensity(100) lcolor(none%50) lwidth(none)) ///
		 (line fpos_pred  ps_period if tr_sorted==1, sort ylabel(-.8(.2).4) lcolor(black) lwidth(thick) lpattern(dash) ) ///
		(line fpos_pred  ps_period if tr_sorted==2, sort ylabel(-1(1)14) lcolor(blue) lwidth(thick) lpattern(dash))  ///
		(line fpos_pred  ps_period if tr_sorted==3, sort ylabel(8(1)17) xlabel(1 (1) 10)  lcolor(red) lwidth(thick) lpattern(dash))  ///
		(line fpos_a_gr_pe_mean  ps_period if tr_sorted==1, sort ylabel(-.8(.2).4) lcolor(black) lwidth(thick) ) ///
		(line fpos_a_gr_pe_mean  ps_period if tr_sorted==2, sort ylabel(-1(1)14) lcolor(blue) lwidth(thick)  ytitle(Forward Position) )  ///
		(line fpos_a_gr_pe_mean ps_period if tr_sorted==3, sort ylabel(8(1)16) xlabel(1 (1) 10)  lcolor(red) lwidth(thick)), legend(order(6 "T1: 55-65" 7 "T2: 40-80" 8 "T3: 20-100") rows(1))
		


************************************************************************
* Table 8. Implied level of absolute risk aversion
local name = "aa1221.doc"
* All periods (1-10)
reg RA_implied_pe  ones if tag_per_auction_gr_pe_ph==1 , noc vce(cluster au_gr_id)
outreg2 using `name' ,  label //1

reg RA_implied_pe  tr1 tr2 tr3 if tag_per_auction_gr_pe_ph==1 , noc vce(cluster au_gr_id)
outreg2 using `name' ,  label //2

* Last periods (6-10)
reg RA_implied_pe  ones if tag_per_auction_gr_pe_ph==1 & ps_period> 5, noc vce(cluster au_gr_id)
outreg2 using `name' ,  label //3
reg RA_implied_pe  tr1 tr2 tr3 if tag_per_auction_gr_pe_ph==1 & ps_period> 5, noc vce(cluster au_gr_id)
outreg2 using `name' ,  label //4

* test  are the implied RAs different?
quietly reg RA_implied_pe  tr1 tr2 tr3 if tag_per_auction_gr_pe_ph==1 , noc vce(cluster au_gr_id)
test (tr1=tr2=tr3)
quietly reg RA_implied_pe  tr1 tr2 tr3 if tag_per_auction_gr_pe_ph==1 & ps_period> 5, noc vce(cluster au_gr_id)
test (tr1=tr2=tr3)
* non-parametric test  are the implied RAs different?
kwallis RA_implied if tag_per_auction_gr_ph==1 , by(tr_sorted)  
kwallis RA_implied5 if tag_per_auction_gr_ph5==1 , by(tr_sorted)  






* outreg2 using RAimplied.doc , see label




***************************************************************************
***************************************************************************
* Footnotes
***************************************************************************





* Footnote 25 As a robustness test, a Jonckheere–Terpstra test was used. The test rejected any possible alternative order of treatments with a significance of p=0.03.
jonter fpremium_rel_a_gr if  tag_per_auction_gr==1, by(tr_sorted) 



* Footnote 23 Using only the last 5 period leads to qualitatively identical results.
* * Figure 3: The forward premium 
* * a) By treatment and by group
twoway 	(rbar fpremium_rel_a_gr5_lb95 fpremium_rel_a_gr5_ub95 tr_sorted if tr_sorted==1  , sort  ///
 		 fcolor(black%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
		 (rbar fpremium_rel_a_gr5_lb95 fpremium_rel_a_gr5_ub95 tr_sorted if tr_sorted==2  , sort  ///
 		 fcolor(blue%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
		 (rbar fpremium_rel_a_gr5_lb95 fpremium_rel_a_gr5_ub95 tr_sorted if tr_sorted==3  , sort  ///
 		 fcolor(red%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
		(scatter fpremium_rel_a_gr5 tr_sorted if tr_sorted==1, sort ylabel(-.8(.2).4) mcolor(black)) ///
		(scatter fpremium_rel_a_gr5 tr_sorted if tr_sorted==2, sort ylabel(-.8(.2).4) mcolor(blue)) ///
		(scatter fpremium_rel_a_gr5 tr_sorted if tr_sorted==3, sort ylabel(-.8(.2).4) mcolor(red)) ///
		(scatter fpremium_rel_a_gr5_mean tr_sorted if tr_sorted==1, msize(huge) mcolor(black)) ///
		(scatter fpremium_rel_a_gr5_mean tr_sorted if tr_sorted==2, msize(huge) mcolor(blue)) ///
		(scatter fpremium_rel_a_gr5_mean tr_sorted if tr_sorted==3, msize(huge) mcolor(red)) , ytitle(Forward Premium (%)) ///
           ytitle(, size(vlarge)) ylabel(-.8(.2).4, labsize(large)) ymtick(, labsize(large)) xtitle(, size(vlarge)) ///
		   xlabel(#3, labsize(large) valuelabel ticks) xmtick(, labsize(large) ) ///
		   legend(order(1 "groups" 4 "treatments")  cols(2)  subtitle("Averaged over:")) legend(off)


* * b) By treatment and period
* * Same as with 10 periods, just leave out the first 5 results.


* *** Table 7. Test results using non-parametric tests 
* ** Relative Forward Premium 
* * Hypothesis 1
signrank fpremium_rel_a_gr5_tr1 = 0
signrank fpremium_rel_a_gr5_tr2 = 0
signrank fpremium_rel_a_gr5_tr3 = 0

* * Hypothesis 2
ranksum fpremium_rel_a_gr5, by(tr2_vs_tr1)
ranksum fpremium_rel_a_gr5, by(tr3_vs_tr2)
ranksum fpremium_rel_a_gr5, by(tr3_vs_tr1)

* ** Forward Positions
* * Hypothesis 3a
signrank fpos_a_gr5_tr1 = 0
signrank fpos_a_gr5_tr2 = 0
signrank fpos_a_gr5_tr3 = 0

* * Hypothesis 3b
signrank fpos_a_gr5_tr1 = 14.6
signrank fpos_a_gr5_tr2 = 15
signrank fpos_a_gr5_tr3 = 16.3


* * However, as expected, they do not differ much over the treatments. 
ranksum fpos_a_gr5, by(tr2_vs_tr1)
ranksum fpos_a_gr5, by(tr3_vs_tr2)
ranksum fpos_a_gr5, by(tr3_vs_tr1)
jonter fpos_a_gr5 if  tag_per_auction_gr5==1, by(tr_sorted) 


* * footnote 25 As a robustness test, a Jonckheere–Terpstra test was used. The test rejected any possible alternative order of treatments with a significance of p=0.03.
jonter fpremium_rel_a_gr5 if  tag_per_auction_gr5==1, by(tr_sorted) 


* * Figure 5: The forward position per treatment, predicted and observed.		
* * a) By treatment and by group
twoway 	(rbar fpos_a_gr5_lb95 fpos_a_gr5_ub95 tr_sorted if tr_sorted==1  , sort  ///
 		 fcolor(black%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
		 (rbar fpos_a_gr5_lb95 fpos_a_gr5_ub95 tr_sorted if tr_sorted==2  , sort  ///
 		 fcolor(blue%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
		 (rbar fpos_a_gr5_lb95 fpos_a_gr5_ub95 tr_sorted if tr_sorted==3  , sort  ///
 		 fcolor(red%20) fintensity(20) lcolor(none%50) lwidth(none)) ///
	(scatter fpos_pred  tr_sorted if tr_sorted==1, sort ylabel(-.8(.2).4) mcolor(black) lwidth(thick) lpattern(dash)  msize(vhuge) msymbol(square) ) ///
		(scatter fpos_pred  tr_sorted if tr_sorted==2, sort ylabel(-1(1)14) mcolor(blue) lwidth(thick) lpattern(dash) msize(vhuge) msymbol(square))  ///
		(scatter fpos_pred  tr_sorted if tr_sorted==3, sort ylabel(8(1)17)   mcolor(red) lwidth(thick) lpattern(dash) msize(vhuge) msymbol(square)) ///
		(scatter fpos_a_gr5_mean tr_sorted if tr_sorted==1, msize(huge) mcolor(black)) ///
		(scatter fpos_a_gr5_mean tr_sorted if tr_sorted==2, msize(huge) mcolor(blue)) ///
		(scatter fpos_a_gr5_mean tr_sorted if tr_sorted==3, msize(huge) mcolor(red)), ytitle(Forward Position) ///
           ytitle(, size(vlarge)) ylabel(10(1)16, labsize(large)) ymtick(, labsize(large)) xtitle(, size(vlarge)) ///
		   xlabel(#3, labsize(large) valuelabel ticks) xmtick(, labsize(large) ) ///
		   legend(order(1 "groups" )  cols(2)  subtitle("Averaged over:"))	 legend(off) xscale(range(1 3.15)) 

* * b) By treatment and period
* * Same as with 10 periods, just leave out the first 5 results.
*************************************************************************************
******************************
******************************



