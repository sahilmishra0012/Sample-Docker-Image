def get_person(bg):
    data=[('Sahil', 'Mishra', 'O+', '12 Madhupuram Colony, IIM Road off Sitapur Road, Lucknow, 226020', '7007059528'),
          ('Shikhar', 'Mishra', 'B+', '12 Madhupuram Colony, IIM Road off Sitapur Road, Lucknow, 226020', '9793717669'),
          ('Vinod Kumar', 'Mishra', 'B+', '12 Madhupuram Colony, IIM Road off Sitapur Road, Lucknow, 226020', '9935861001')]

    data1=[]
    for i in data:
        if i[2]==bg:
            print(i)
            data1.append(i)
        
    return data1
