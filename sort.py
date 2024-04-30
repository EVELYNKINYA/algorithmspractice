def solution(array_of_users, target_id):
  unread_messages = []
  read_messages = []

  for user in array_of_users:
    if user['id'] == target_id:
        # Check if the user has any messages
        for message in user['messages']:
            # Check if the message has been read
            if  message['read']:
                # Add the message to the read messages
                 read_messages.append(message)
            else:
                unread_messages.append(message)
       #Add a tag to the messages
        for user in unread_messages:
           user['Tag']='unread'
        for user in read_messages:
           user['Tag']='read'

# 
        sorted_array_of_users = read_messages + unread_messages
      
        return sorted_array_of_users  

 # Input examples 
dataArray = [
    {
        "id": 30,
        "username": "Ruth.Nduta",
        "email": "ruthnduta891@gmail.com",
        "messages": [
            {
                "receipient_id": 45,
                "read": False,
                "user_id": 30
            },
            {
                "receipient_id": 3,
                "read": False,
                "user_id": 30
            },
            {
                "receipient_id": 112,
                "read": False,
                "user_id": 30
            }
        ]
    },
    {
        "id": 31,
        "username": "Pascaline.Chumba",
        "email": "pjerono56@gmail.com",
        "messages": []
    },
    {
        "id": 45,
        "username": "Josephbill",
        "email": "josephbill00@gmail.com",
        "messages": [
            {
                "msg_id": 3,
                "read": True,
                "user_id": 45
            }
        ]
    },
    {
        "id": 26,
        "username": "Simon.Thuo",
        "email": "simonthuo85@gmail.com",
        "messages": []
    },
    {
        "id": 27,
        "username": "Christine.Kiage",
        "email": "christinekiage@gmail.com",
        "messages": [
                  {
                "msg_id": 45,
                "read": False,
                "user_id": 27
            },
            {
                "msg_id": 3,
                "read": False,
                "user_id": 27
            },
            {
                "msg_id": 112,
                "read": False,
                "user_id": 27
            }
            ]
    }
    ]

 
solution= solution(dataArray, 27)
    
print(solution) 