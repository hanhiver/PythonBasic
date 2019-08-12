# warnings test program. 
# Use python -W all to call the turn_left() function. 
# It will print out a deprecation warning message. 


import warnings

class Car(object):
    def turn_left(self):
        """
        Turn the car left. 
        .. deprecated:: 1.1
           Use :func: `turn` instead with the derection argument set to "left". 
        """
        warnings.warn("turn_left is deprecated, use turn instead.", DeprecationWarning)

    def turn(self, direction):
        """
        Turn the car in some direction. 

        :param direction: the direction to turn to. 
        :type direction: str
        """
        pass


