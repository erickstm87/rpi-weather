import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code:', r.status_code)

response_dict = r.json()
repo_dicts = response_dict['items']

names, stars, plot_dicts = [], [], []
for repo in repo_dicts:
    names.append(repo['name'])
    stars.append(repo['stargazers_count'])
    description = repo['description']
    if(not description):
        description = 'description not found'
    plot_dict = {
        'value': repo['stargazers_count'],
        'label': description,
        'xlink': repo['html_url']
    }
    plot_dicts.append(plot_dict)

my_style = LS('#e6e600', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
#chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('/home/pi/rpi-weather/api-calls/python_repos.svg')
