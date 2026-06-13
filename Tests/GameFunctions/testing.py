from GameFunctions import gamefunctions
from GameFunctions.gamefunctions import makeoffer
from Setup.setup import setupboxes
from Box.box import Box
import pytest
# TODO - Rename file to test_game_functions

class TestValidateInput:
    def test_validate_input_valid(self):
        user_input = '2'
        result = gamefunctions.validateinput(user_input)
        assert result

    def test_validate_input_invalid_not_numeric(self):
        test_input = 'b'
        result = gamefunctions.validateinput(test_input)
        assert not result

    def test_validate_input_too_small(self):
        test_input = '0'
        result = gamefunctions.validateinput(test_input)
        assert not result

    def test_validate_input_too_large(self):
        test_input = '25'
        result = gamefunctions.validateinput(test_input)
        assert not result


def setup():
    return setupboxes()


class TestRemoveBox:

    def test_remove_box(self):
        test_boxes = setupboxes()
        gamefunctions.removebox(test_boxes, 1)
        assert not test_boxes.__contains__(1)

    def test_remove_box_no_box_found(self):
        test_boxes = setupboxes()
        result = gamefunctions.removebox(test_boxes,0)
        assert not result

    def test_cant_remove_box_twice(self):
        test_boxes = setupboxes()
        result = gamefunctions.removebox(test_boxes, 1)
        assert result
        result = gamefunctions.removebox(test_boxes, 1)
        assert not result

class TestMakeChoice:
    # TODO - Look into how to test user input
    pass

class TestSwapBox:
    box_1 = {1:1}
    box_2 = {2:100}
    # TODO - Look into how to test user input

class TestMakeOffer:
    def test_make_offer_small_sample(self):
        test_boxes = {
            1:Box(1,1),
            2: Box(2, 5),
            3: Box(3, 10),
            4: Box(4, 20),
            5: Box(5, 50),
            6: Box(6, 100),
        }
        user_box = test_boxes.pop(1)
        offer = 0.00
        for box in test_boxes:
            offer += test_boxes[box].value
        offer = (offer + user_box.value) / len(test_boxes) + 1
        assert offer == 0
        offer = makeoffer(test_boxes,user_box.value)
        assert offer == 0.31