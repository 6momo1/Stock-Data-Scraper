import functions
import sql_functions


# sql_functions.update('TSLA','Sector','Technology')

# li = ['TSLA','FB']
# for x in li:
# 	sql_functions.insert_token_data(x)


sql_functions.insert_token_data('MA')
# sql_functions.drop_token('GM')


def table(token):
    try:
        url = 'https://finviz.com/quote.ashx?t={}'.format(token)
        headers = {
            'User-Agent': "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        table = soup.find_all("table", attrs={'class': "snapshot-table2"})
        lst = []
        for row in range(12):
            for col in range(12):
                if (col % 2) == 0:
                    lst.append(urlify(table[0].find_all('tr')[
                               row].find_all('td')[col].text))
                else:
                    lst.append(table[0].find_all('tr')[
                               row].find_all('td')[col].text)

        dic = {"Token": token}

        temp_dic = {lst[i]: lst[i+1] for i in range(0, len(lst), 2)}
        dic.update(temp_dic)
        return dic
    except Exception as e:
        print(e)

        # <table> has one <tbody>
        # table[0] = <tbody>
        # #in <tbody> there are 12 rows of <tr>, row
        # table1 = table[0].find_all('tr')
        # #in each <tr> there are 12 <td>, column
        # table2 = table1[0].find_all('td')
