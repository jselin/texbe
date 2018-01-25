from decimal import *

"""
Length shrinkage (m) = (Length + Headings/Hems) / 100 x Length shrinkage (%)										
Width shrinkage (cm) = Width / 100 x Width shrinkage (%)										
Length take-up (m) =  ((Length + Headings/Hems + Length shringage (m) + Fringes) x Number of designs + Test Peace x Number of test pieces + Loom waste + Cutting Margin) / 100 x Length take up (%)										
Width draw-in (cm) = (Width + Width shrinkage (cm)) / 100 * Width draw-in (%)										
Fabric lenght (m) = (Lenght + Headings/Hems + Lenght shrinkage (m)) x Number of designs + Length of Test Piece x Number of test pieces + Length take-up (m)										
										
Warp length (m) = (Length + Headings/Hems + Length shringage (m) + Fringes) x Number of designs + Length of Test Piece x Number of test pieces + Loom waste + Cutting Margin + Length take-up (m)										
Warp width (m) = Width + Width shrinkage (cm) + Width draw-in (cm)										
Number of ends = Warp width (cm) x Ends per cm										
Number of picks = Warp length (m) x 100 x Picks per cm										
										
Warp demand (g) = Ends per cm x Warp width (cm) x Warp lenght (m) x Yarn TEX number / 1000 										
Weft demand (g) = Picks per cm tiheys x Warp width (cm) x Fabric length (m) x Yarn TEX number /1000										
"""


def plan_calculate(i):
    # Takes in Model instance and modifies it deirectly FIXME possibly evil

    length_shrinkage_m = (i.finished_lenght_m + i.headings_hems_lenght_m) * Decimal(i.lenght_shrinkage_p / 100)
    #print("length_shrinkage_m: %f", length_shrinkage_m)
    width_shrinkage_cm = i.finished_width_cm * Decimal(i.width_shrinkage_p / 100)
    #print("width_shrinkage_cm: %f", width_shrinkage_cm)
    length_take_up_m = ((i.finished_lenght_m + i.headings_hems_lenght_m + length_shrinkage_m + \
        i.fringe_lenght_m) * i.number_of_desigs + (i.test_piece_lenght_m * i.number_of_test_pieces) + \
        i.loom_waste_lenght_m + i.cutting_margin_m) * Decimal(i.lenght_take_up_p / 100)
    #print("length_take_up_m: %f", length_take_up_m)
    width_draw_in_cm = (i.finished_width_cm + width_shrinkage_cm) * Decimal(i.width_draw_in_p / 100)
    #print("width_draw_in_cm: %f", width_draw_in_cm)
    fabric_lenght_m = (i.finished_lenght_m + i.headings_hems_lenght_m + length_shrinkage_m) * \
        i.number_of_desigs + i.test_piece_lenght_m * \
        i.number_of_test_pieces + length_take_up_m
    #print("fabric_lenght_m: %f", fabric_lenght_m)
    i.warp_lenght_m = two_decimals((i.finished_lenght_m + i.headings_hems_lenght_m + length_shrinkage_m + i.fringe_lenght_m) * \
        i.number_of_desigs + (i.test_piece_lenght_m * i.number_of_test_pieces) + \
        i.loom_waste_lenght_m + i.cutting_margin_m + length_take_up_m)


    i.warp_width_cm = one_decimal(i.finished_width_cm + width_shrinkage_cm + width_draw_in_cm)
    i.number_of_ends = no_decimal(i.warp_width_cm * i.ends_per_cm)
    i.number_of_pics = no_decimal(i.warp_lenght_m * (i.picks_per_cm * 100))
    
    i.warp_demand_g = no_decimal(i.ends_per_cm * i.warp_width_cm * i.warp_lenght_m * i.warp_yarn.tex_number / 1000)
    #print("i.warp_yarn.tex_number: %f", i.warp_yarn.tex_number)
    i.weft_demand_g = no_decimal(i.picks_per_cm * i.warp_width_cm * fabric_lenght_m * i.weft_yarn.tex_number /1000)

def no_decimal(d):
    return Decimal(d).quantize(Decimal('1'), rounding=ROUND_UP)
def one_decimal(d):
    return Decimal(d).quantize(Decimal('0.1'), rounding=ROUND_UP)
def two_decimals(d):
    return Decimal(d).quantize(Decimal('0.01'), rounding=ROUND_UP)



""""
        finished_lenght_m, headings_hems_lenght_m=0, lenght_shrinkage_p,
        fringe_lenght_m=0, finished_width_cm, width_shrinkage_p,
        number_of_desigs=1, test_piece_lenght_m=0, number_of_test_pieces=1,
        loom_waste_lenght_m, cutting_margin_m, lenght_take_up_p,
        width_draw_in_p, selvedge_warps, warp_tex, weft_tex,
        picks_per_cm, ends_per_cm):
    return (
        {'warp_lenght_m': warp_lenght_m, 'warp_width_cm': warp_width_cm,
        'number_of_ends': number_of_ends, 'number_of_pics': number_of_pics,
        'warp_demand_g': warp_demand_g, 'weft_demand_g': weft_demand_g})
"""
