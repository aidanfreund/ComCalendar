from RequestValidator import RequestValidator
from Operator import Operator


class LoginMenu:
    # Basic login func
    def login(self,username,password):
        if(RequestValidator.validate_login(username, password)):
            return Operator.validate_login
       
    # Returns bool if successful
    def create_profile(self, username, password):
        return RequestValidator.validate_call((username,password))
    
   
    
        
   
    

