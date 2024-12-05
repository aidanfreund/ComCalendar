from RequestValidator import RequestValidator
from Operator import Operator


class LoginMenu:
    # Basic login func, returns a profile object
    def login(self,username,password):
        if(RequestValidator.validate_login(username, password)):
            Operator.login(username,password)
       
    # Returns bool if successful
    def create_profile(self, username, password):
        return RequestValidator.validate_call((username,password))
    
   
    
        
   
    

