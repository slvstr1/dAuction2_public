********************************************************
* First run do1_ initialize_2019.11.06.do
********************************************************


* Figure 3: The forward premium 
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


*** Table 6. Test results using non-parametric tests 
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


* footnote 21 As a robustness test, a Jonckheere–Terpstra test was used. The test rejected any possible alternative order of treatments with a significance of p=0.03.
jonter fpremium_rel_a_gr if  tag_per_auction_gr==1, by(tr_sorted) 


* Figure 4: The forward position per treatment, predicted and observed.		
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
		
******************************
******************************
* Footnote 19 Using only the last 5 period leads to qualitatively identical results.
*************************************************************************************
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
* * no difference


* *** Table 6. Test results using non-parametric tests 
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


* * footnote 21 As a robustness test, a Jonckheere–Terpstra test was used. The test rejected any possible alternative order of treatments with a significance of p=0.03.
jonter fpremium_rel_a_gr5 if  tag_per_auction_gr5==1, by(tr_sorted) 


* * Figure 4: The forward position per treatment, predicted and observed.		
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
* * no difference
*************************************************************************************
******************************
******************************

