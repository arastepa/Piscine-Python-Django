def periodic_table():
    file = open('periodic_table.txt', 'r')
    row = ''
    prev = 0
    while True:
        line = file.readline()
        if not line:
            break
        name = line.strip().split('=')[0].strip()
        data = line.strip().split(',')
        pos = data[0].split('=')
        pos = pos[1].split(':')[1]
        number = data[1].split(':')[1]
        small = data[2].split(':')[1]
        molar = data[3].split(':')[1]
        if int(pos) == 0:
            row += '<tr style = "white-space: nowrap; overflow-x: auto;">'
        diff = int(pos) - int(prev)
        if diff > 1:
            for i in range(int(prev), int(pos)-1):
                row += '<td style = "width:150px; height: 200px; display: inline-block;"></td>'
        row += f'''<td style = "width:150px; height: 200px; display: inline-block;"><h4>{name}</h4><ul>
                <li>{small}</li>
                <li>{number}</li>
                <li>{molar}</li>
                </ul></td>'''
        if int(pos) == 18:
            row += '</tr>'
        prev = pos
    html = f''' <!DOCTYPE html>
<html lang = 'en'><head><title>periodic table</title>
    <style>
        table, tr, td{{
            border: 1px solid black;
            border-collapse: collapse;
            font-size: 20px;
        }}
    </style>
    </head><body><table>{row}</table></body></html> '''
    with open('periodic_table.html', 'w') as file:
        file.write(html)
if __name__== '__main__':
    periodic_table()