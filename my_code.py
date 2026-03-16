import pytest


def fix_phone_num(phone_num_to_fix):
  if len(phone_num_to_fix) != 10:
    raise ValueError("Can only format numbers that are exactly 10 digits long")
  if not phone_num_to_fix.isdigit():
    raise ValueError("Can only format strings containing digits only")

  area_code = phone_num_to_fix[0:3]
  three_part = phone_num_to_fix[3:6]
  four_part = phone_num_to_fix[6:]
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part
  return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'

def test_fix_phone_num_format_error():
  with pytest.raises(ValueError):
    fix_phone_num("555-442-98761")
  with pytest.raises(ValueError):
    fix_phone_num("(3213) 654 3333")

def test_fix_phone_num_non_digit():
  with pytest.raises(ValueError):
    fix_phone_num("334dfdee45")
  with pytest.raises(ValueError):
    fix_phone_num("abcdefghij")