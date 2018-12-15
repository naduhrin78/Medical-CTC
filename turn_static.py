ans = ''


def statify(line, edit):
    if edit and edit.find('#') == -1 and edit.find('http') == -1:
        inject = "{% static '" + edit + "' %}"

        line = line.replace(edit, inject)

    return line


with open('template/md_ctc/index.html', encoding='utf-8', mode='r') as f:
    for line in f:

        edit = ''

        if line.find('src=') > -1:
            edit = line.split('src="')[1].split('"')[0]

        if line.find('href=') > -1:
            edit = line.split('href="')[1].split('"')[0]

        line = statify(line, edit)

        ans += line

with open('template/md_ctc/result.html', encoding='utf-8', mode='w') as f:
    f.write(ans)
