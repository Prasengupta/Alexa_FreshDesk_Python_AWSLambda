import requests
import json
def GetFreshDeskCount():	
	api_key = "*******"
	domain = "*******"
	password = "x"
	lStatus = []
	# Return the tickets that are new or opend & assigned to you
	# If you want to fetch all tickets remove the filter query param
	r = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets", auth = (api_key, password))
	if r.status_code == 200:
		#print "Request processed successfully, the response is given below"
		data = r.content
		##print "intial data==>",data
		data_set = json.loads(data)
		#print " "
		#print " "
		#print "full data==>",data_set
		# for dictItem in data_set:
		# 	#print data_set.get('id')
		##print "find==>",data_set[0].get("fr_escalated")
		#print "Lenght====>",len(data_set)
		for dictItem in data_set:
			Status_count = dictItem.get("status")
			#print "Status value",Status_count
			if Status_count==2:
				lStatus.append(Status_count)
				#print "List of 2's",lStatus
				lenght_open_tickets = len(lStatus)
				#print "final lenght===>",lenght_open_tickets
	else:
		#print "Failed to read tickets, errors are displayed below,"
		response = json.loads(r.content)
		#print response["errors"]
		#print "x-request-id : " + r.headers['x-request-id']
		#print "Status Code : " + str(r.status_code)
	return lenght_open_tickets
# a = GetFreshDeskCount()
# print a