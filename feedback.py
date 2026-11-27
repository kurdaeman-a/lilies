class FeedBack:
    
    """feedback submitted by a customer"""
    
# here we have added message too, but in our class it does not contain that.
    def __init__(self,feedback_id, message):
        self._feedback_id = feedback_id
        self._message = message

    """Display the feedback id and message"""

    def display_feedback(self):
        print(f"Feedback ID : {self._feedback_id}")
        print(f"Message : {self._message}")   
        
feedback1= FeedBack(101, "I like your website design:)")     
feedback1.display_feedback()   