from RequestValidator import RequestValidator


class LoginMenu:
    # Basic login func
    def login(self,username,password):
        if(RequestValidator.validate_login(username, password)):
            pass # Do something
       
    # Returns bool if successful
    def create_profile(self, username, password):
        return RequestValidator.validate_create_account((username,password))
    
   
    
        
   
    

