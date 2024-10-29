import Profile
class LoginMenu:
    # Basic login func
    def login(self,username,password):
        if(_validate_login(self,username,password)):
            return True
        else:
            return False
    def create_profile(self, username, password):
        pass
    # Validation to be discussed
    def _validate_login(self,username,password):
        pass
    
        
   
    

