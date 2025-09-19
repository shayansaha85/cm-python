

file = open('TeradataOutput.log', 'r')
content = file.readlines()
file.close()

filtered_data = []
for x in content:
      filtered_data.append(x.strip()) # ['ActiveStore 450', 'InactiveStore 70']

csv_content = "StoreStatus,Count"
for data in filtered_data:
      d = data.split() #  ['ActiveStore', '450']
      status = d[0] # ActiveStore
      statusCount = d[-1] # 450
      #ActiveStore,450
      output = status + "," + statusCount 
      csv_content = csv_content + output

file2 = open('teradataOutput.csv', 'w')
file2.write(csv_content)
file2.close()

