from Operator import Operator

class RequestValidator:
    
    # Validation method to be defined
    @classmethod
    def validate_login(cls, username,password):
        pass

    # Validation method to be discussed
    @classmethod
    def validate_call(cls, input):
        return isinstance(input,str)