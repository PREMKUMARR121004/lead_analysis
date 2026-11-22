from pydantic import BaseModel
from enum import Enum


class Intent(str,Enum):
   BUYING="Buying",
   SELLING="Selling",
   RENTING="Renting"
   GENERAL_ENQUIRY="General enquiry"
   NOT_INTERESTED="Not interested"

class Sentiment(str,Enum):
   POSITIVE="positive"
   NEGATIVE="negative"
   NEUTRAL="neutral"







class CustomerCreate(BaseModel):
   location:str|None=None
   property_type:str|None=None
   budget:int|None=None
   timeline:str|None=None
   intent:Intent
   sentiment:Sentiment
   additional_notes:str|None=None
