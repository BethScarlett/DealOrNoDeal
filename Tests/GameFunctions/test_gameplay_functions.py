from GameFunctions import gamefunctions
from GameFunctions.gamefunctions import makeoffer
from Setup.setup import setupboxes
from Box.box import Box

def setup():
    return setupboxes()

class TestValidateInput:
    """
        Test that user inputs conform to preset validations,
        and invalid inputs are blocked
    """
    def test_validate_input_valid(self):
        """
            Test input - valid
        """
        user_input = '2'
        result = gamefunctions.validateinput(user_input)
        assert result

    def test_validate_input_must_be_numeric(self):
        """
            Test input - Must be numeric
        """
        test_input = 'b'
        result = gamefunctions.validateinput(test_input)
        assert not result

    def test_validate_input_in_range(self):
        """
            Test input - In range (1-24)
        """

        # Lower limit
        test_input = '0'
        result = gamefunctions.validateinput(test_input)
        assert not result

        # Upper limit
        #TODO - Look into moving guesses to be numbers - Should already be?
        test_input = 25
        result = gamefunctions.validateinput(test_input)
        assert not result

class TestRemoveBox:
    """
        Test box removal logic to ensure boxes are removed when valid
    """
    def test_remove_box(self):
        """
            Test user can remove chosen box
        """
        test_boxes = setupboxes()
        gamefunctions.removebox(test_boxes, 1)
        assert not test_boxes.__contains__(1)

    def test_cant_remove_box_twice(self):
        """
            Test user can't remove same box twice
        """
        test_boxes = setupboxes()
        result = gamefunctions.removebox(test_boxes, 1)
        # TODO - Look at possibly reworking remove box to be more helpful i.e. don't just return true/false
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
    """
        Test logic which determines the offer given to the player
    """
    def test_make_offer_small_sample(self):
        """
            Test offer against small sample
        """
        test_boxes = {
            1:Box(1,1),
            2: Box(2, 5),
            3: Box(3, 10),
            4: Box(4, 20),
            5: Box(5, 50),
            6: Box(6, 100),
        }
        user_box = test_boxes.pop(1)
        offer = makeoffer(test_boxes, user_box.value)
        assert offer == 0.38