from django.test import TestCase
from planner.models import Yarn, Plan
from planner.calculate import plan_calculate

# Create your tests here.
class YarnTestCase(TestCase):
    def setUp(self):
        pass
    def test_TEX(self):
        """Test TEX"""
        yarn = Yarn(numbering_system='TEX', number='2/2')
        self.assertEqual(yarn.tex_number, 4)
        yarn = Yarn(numbering_system='TEX', number='2')
        self.assertEqual(yarn.tex_number, 2)
        yarn = Yarn(numbering_system='TEX', number='2x2')
        self.assertEqual(yarn.tex_number, 4)
        yarn = Yarn(numbering_system='TEX', number='2 / 2')
        self.assertEqual(yarn.tex_number, 4)
        yarn = Yarn(numbering_system='TEX', number='2*2')
        self.assertEqual(yarn.tex_number, 4)
        yarn = Yarn(numbering_system='TEX', number='2 2')
        self.assertNotEqual(yarn.tex_number, 4)
        yarn = Yarn(numbering_system='TEX', number='2.2')
        self.assertNotEqual(yarn.tex_number, 2.2)
        yarn = Yarn(numbering_system='TEX', number='2,2')
        self.assertNotEqual(yarn.tex_number, 2.2)
    def test_NE(self):
        """Test NE"""
        yarn = Yarn(numbering_system='NE', number='4')
        self.assertAlmostEqual(float(yarn.tex_number), 590.5412474/4)
        yarn = Yarn(numbering_system='NE', number='4/2')
        self.assertAlmostEqual(float(yarn.tex_number), 590.5412474/2)
    def test_NEL(self):
        """Test NEL"""
        yarn = Yarn(numbering_system='NEL', number='4')
        self.assertAlmostEqual(float(yarn.tex_number), 1653.515493/4)
        yarn = Yarn(numbering_system='NEL', number='30/2')
        self.assertAlmostEqual(float(yarn.tex_number), 1653.515493/15)
    def test_NM(self):
        """Test NM"""
        yarn = Yarn(numbering_system='NM', number='4')
        self.assertEqual(yarn.tex_number, 1000/4)
    def test_DEN(self):
        """Test DEN"""
        yarn = Yarn(numbering_system='DEN', number='40')
        self.assertAlmostEqual(float(yarn.tex_number), 40/9)



class PlanTestCase(TestCase):
    def setUp(self):
        pass
    def test_plan_calculation(self):
        p = Plan()
        # Design
        p.finished_lenght_m = 1
        p.headings_hems_lenght_m = 0
        p.lenght_shrinkage_p = 0
        p.fringe_lenght_m = 0
        p.finished_width_cm = 100
        p.width_shrinkage_p = 0
        p.number_of_designs = 1

        # Weawing
        p.test_piece_lenght_m = 0
        p.number_of_test_pieces = 0
        p.loom_waste_lenght_m = 0
        p.cutting_margin_m = 0
        p.lenght_take_up_p = 0
        p.width_draw_in_p = 0
        p.selvedge_warps = 0

        # Yarns
        p.warp_yarn = Yarn(numbering_system='TEX', number='12/2')
        p.weft_yarn = Yarn(numbering_system='TEX', number='12/2')
        p.picks_per_cm = 20
        p.ends_per_cm = 20

        plan_calculate(p)

        # On loom calculated
        self.assertEqual(p.warp_lenght_m, 1)
        self.assertEqual(p.number_of_ends, 2000 )
        self.assertEqual(p.warp_width_cm, 100)
        self.assertEqual(p.number_of_pics, 2000)

        # Demand calculated
        self.assertEqual(p.warp_demand_g, 48)
        self.assertEqual(p.weft_demand_g, 48)

    def test_nel_yarn_demand_1(self):
        p = Plan()
        # Design
        p.finished_lenght_m = 9
        p.headings_hems_lenght_m = 0
        p.lenght_shrinkage_p = 0
        p.fringe_lenght_m = 0
        p.finished_width_cm = 45
        p.width_shrinkage_p = 0
        p.number_of_designs = 1

        # Weawing
        p.test_piece_lenght_m = 0
        p.number_of_test_pieces = 0
        p.loom_waste_lenght_m = 0
        p.cutting_margin_m = 0
        p.lenght_take_up_p = 0
        p.width_draw_in_p = 0
        p.selvedge_warps = 0

        # Yarns
        p.warp_yarn = Yarn(numbering_system='NEL', number='30/2')
        p.weft_yarn = Yarn(numbering_system='NEL', number='30/2')
        p.picks_per_cm = 14
        p.ends_per_cm = 14

        plan_calculate(p)

        # On loom calculated
        self.assertEqual(p.warp_lenght_m, 9)
        self.assertEqual(p.number_of_ends, 630 )
        self.assertEqual(p.warp_width_cm, 45)
        self.assertEqual(p.number_of_pics, 12600)

        # Demand calculated
        self.assertEqual(p.warp_demand_g, 630)
        self.assertEqual(p.weft_demand_g, 630)

    def test_tex_yarn_demand_1(self):
        p = Plan()
        # Design
        p.finished_lenght_m = 9
        p.headings_hems_lenght_m = 0
        p.lenght_shrinkage_p = 0
        p.fringe_lenght_m = 0
        p.finished_width_cm = 45
        p.width_shrinkage_p = 0
        p.number_of_designs = 1

        # Weawing
        p.test_piece_lenght_m = 0
        p.number_of_test_pieces = 0
        p.loom_waste_lenght_m = 0
        p.cutting_margin_m = 0
        p.lenght_take_up_p = 0
        p.width_draw_in_p = 0
        p.selvedge_warps = 0

        # Yarns
        p.warp_yarn = Yarn(numbering_system='TEX', number='30/2')
        p.weft_yarn = Yarn(numbering_system='TEX', number='30/2')
        p.picks_per_cm = 14
        p.ends_per_cm = 14

        plan_calculate(p)

        # On loom calculated
        self.assertEqual(p.warp_lenght_m, 9)
        self.assertEqual(p.number_of_ends, 630 )
        self.assertEqual(p.warp_width_cm, 45)
        self.assertEqual(p.number_of_pics, 12600)

        # Demand calculated
        self.assertEqual(p.warp_demand_g, 169)
        self.assertEqual(p.weft_demand_g, 169)
    
    def test_tex_yarn_demand_2(self):
        p = Plan()
        # Design
        p.finished_lenght_m = 1.5
        p.headings_hems_lenght_m = 5
        p.lenght_shrinkage_p = 15
        p.fringe_lenght_m = 0
        p.finished_width_cm = 23
        p.width_shrinkage_p = 15
        p.number_of_designs = 2

        # Weawing
        p.test_piece_lenght_m = 0.20
        p.number_of_test_pieces = 1
        p.loom_waste_lenght_m = 0.60
        p.cutting_margin_m = 0
        p.lenght_take_up_p = 0
        p.width_draw_in_p = 0
        p.selvedge_warps = 2

        # Yarns
        p.warp_yarn = Yarn(numbering_system='TEX', number='105')
        p.weft_yarn = Yarn(numbering_system='TEX', number='105')
        p.picks_per_cm = 10
        p.ends_per_cm = 10

        plan_calculate(p)

        # On loom calculated
        self.assertEqual(p.warp_lenght_m, 4.4)
        self.assertEqual(p.number_of_ends, 267)
        self.assertEqual(p.warp_width_cm, 26.5)
        self.assertEqual(p.number_of_pics, 380)

        # Demand calculated
        self.assertEqual(p.warp_demand_g, 123.4)
        self.assertEqual(p.weft_demand_g, 106.4)

def test_nel_yarn_demand_2(self):
        p = Plan()
        # Design
        p.finished_lenght_m = 1.5
        p.headings_hems_lenght_m = 5
        p.lenght_shrinkage_p = 15
        p.fringe_lenght_m = 0
        p.finished_width_cm = 23
        p.width_shrinkage_p = 15
        p.number_of_designs = 2

        # Weawing
        p.test_piece_lenght_m = 0.20
        p.number_of_test_pieces = 1
        p.loom_waste_lenght_m = 0.60
        p.cutting_margin_m = 0
        p.lenght_take_up_p = 0
        p.width_draw_in_p = 0
        p.selvedge_warps = 2

        # Yarns
        p.warp_yarn = Yarn(numbering_system='NEL', number='4')
        p.weft_yarn = Yarn(numbering_system='NEL', number='4')
        p.picks_per_cm = 10
        p.ends_per_cm = 10

        plan_calculate(p)

        # On loom calculated
        self.assertEqual(p.warp_lenght_m, 4.4) 
        self.assertEqual(p.number_of_ends, 267)
        self.assertEqual(p.warp_width_cm, 26.5)
        self.assertEqual(p.number_of_pics, 380)

        # Demand calculated
        self.assertEqual(p.warp_demand_g, 550) 
        self.assertEqual(p.weft_demand_g, 475)

   def test_tex_yarn_demand_3(self):
        p = Plan()
        # Design
        p.finished_lenght_m = 1.2 
        p.headings_hems_lenght_m = 0
        p.lenght_shrinkage_p = 10
        p.fringe_lenght_m = 0.1
        p.finished_width_cm = 50
        p.width_shrinkage_p = 10
        p.number_of_designs = 6

        # Weawing
        p.test_piece_lenght_m = 0.20
        p.number_of_test_pieces = 1
        p.loom_waste_lenght_m = 0.50
        p.cutting_margin_m = 0.25
        p.lenght_take_up_p = 0
        p.width_draw_in_p = 0
        p.selvedge_warps = 2

        # Yarns
        p.warp_yarn = Yarn(numbering_system='TEX', number='305')
        p.weft_yarn = Yarn(numbering_system='TEX', number='305')
        p.picks_per_cm = 7
        p.ends_per_cm = 7

        plan_calculate(p)

        # On loom calculated
        self.assertEqual(p.warp_lenght_m, 9.49)
        self.assertEqual(p.number_of_ends, 387)
        self.assertEqual(p.warp_width_cm, 55)
        self.assertEqual(p.number_of_pics, 5698)

        # Demand calculated
        self.assertEqual(p.warp_demand_g, 1120.2)
        self.assertEqual(p.weft_demand_g, 960.8) #What is the result in code? Manually not matching with result in line 317, why?

   def test_nel_yarn_demand_3(self):
        p = Plan()
        # Design
        p.finished_lenght_m = 1.2 
        p.headings_hems_lenght_m = 0
        p.lenght_shrinkage_p = 5
        p.fringe_lenght_m = 0.1
        p.finished_width_cm = 50
        p.width_shrinkage_p = 5
        p.number_of_designs = 6

        # Weawing
        p.test_piece_lenght_m = 0.20
        p.number_of_test_pieces = 1
        p.loom_waste_lenght_m = 0.50
        p.cutting_margin_m = 0.25
        p.lenght_take_up_p = 5
        p.width_draw_in_p = 5
        p.selvedge_warps = 2

        # Yarns
        p.warp_yarn = Yarn(numbering_system='NEL', number='6')
        p.weft_yarn = Yarn(numbering_system='NEL', number='6')
        p.picks_per_cm = 7
        p.ends_per_cm = 7

        plan_calculate(p)

        # On loom calculated
        self.assertEqual(p.warp_lenght_m, 9.49)
        self.assertEqual(p.number_of_ends, 387)
        self.assertEqual(p.warp_width_cm, 55)
        self.assertEqual(p.number_of_pics, 5698)

        # Demand calculated
        self.assertEqual(p.warp_demand_g, 1020.2)
        self.assertEqual(p.weft_demand_g, 875.1) #What is the result in code? Manually not matching with result in line 279, why?