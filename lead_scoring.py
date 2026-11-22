def calculate_lead_score(intent,timeline,budget):
   score=0

   if intent=="Buying":
      score+=40

   if timeline=="1 month":
      score+=40
   elif timeline in ["2 months","3 months"]:
      score+=30
   elif timeline =="6 months":
      score+=20

   if budget is not None and budget>0:
      score+=20

   if score>=75:
      priority="High"
   elif score>=40:
      priority="medium"
   else:
      priority="low"


   return score,priority

#    print(score,priority)
