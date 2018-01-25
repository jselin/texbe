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
    def test_NE(self):
        """Test NE"""
        yarn = Yarn(numbering_system='NE', number='4')
        self.assertEqual(yarn.tex_number, 590.5/4)
    def test_NEP(self):
        """Test NEP"""
        yarn = Yarn(numbering_system='NEP', number='4')
        self.assertEqual(yarn.tex_number, 720/4)
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
        p.number_of_desigs = 1

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