import pytest
from pytest import approx
import area


def test_square_small_returns_correct_area():
    expected_area = 25
    actual_area = area.square(5)
    assert actual_area == expected_area


def test_square_large_returns_correct_area():
    expected_area = 160000
    actual_area = area.square(400)
    assert actual_area == expected_area


# TODO: Complete this parameterized test to replace the two tests above
# @pytest.mark.parametrize(# TODO)
# def test_square_returns_correct_area(# TODO):
#     actual_area = area.square(length)
#     assert actual_area == expected_area


# TODO: Comment out this test
def test_square_negative_raises_valueerror():
    with pytest.raises(ValueError):
        area.square(-1)


def test_rectangle_small_returns_correct_area():
    expected_area = 60
    actual_area = area.rectangle(15, 4)
    assert actual_area == expected_area


def test_rectangle_large_returns_correct_area():
    expected_area = 70420
    actual_area = area.rectangle(503, 140)
    assert actual_area == expected_area


def test_parallelogram_small_returns_correct_area():
    expected_area = 12
    actual_area = area.parallelogram(3, 4)
    assert actual_area == expected_area


def test_parallelogram_large_returns_correct_area():
    expected_area = 537840
    actual_area = area.parallelogram(1296, 415)
    assert actual_area == expected_area


def test_trapezoid_small_returns_correct_area():
    expected_area = 10
    actual_area = area.trapezoid(2, 3, 4)
    assert actual_area == expected_area


def test_trapezoid_large_returns_correct_area():
    expected_area = 1000
    actual_area = area.trapezoid(20, 30, 40)
    assert actual_area == expected_area


def test_triangle_small_returns_correct_area():
    expected_area = 24
    actual_area = area.triangle(8, 6)
    assert actual_area == expected_area


def test_triangle_large_returns_correct_area():
    expected_area = 10850
    actual_area = area.triangle(700, 31)
    assert actual_area == expected_area


def test_circle_small_returns_correct_area():
    expected_area = approx(254.469)
    actual_area = area.circle(9)
    assert actual_area == expected_area


def test_circle_large_returns_correct_area():
    expected_area = approx(8824.73376)
    actual_area = area.circle(53)
    assert actual_area == expected_area


# TODO: Comment out this test
def test_ellipse_small_returns_correct_area():
    expected_area = approx(131.94689)
    actual_area = area.ellipse(7, 6)
    assert actual_area == expected_area


# TODO: Comment out this test
def test_ellipse_large_returns_correct_area():
    expected_area = approx(3958.40674)
    actual_area = area.ellipse(15, 84)
    assert actual_area == expected_area
