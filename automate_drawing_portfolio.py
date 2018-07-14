import os
from random import shuffle

def automate_portfolio():
    directory = os.fsencode("/Users/austinhunt/Desktop/TheMotherload/huntaj_stu/main/static/main/img/full/drawings")

    path_list = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        filename = "huntaj_stu/main/static/main/img/full/drawings/" + filename

        path_list.append(filename)


    html_div_list = [ ]
    for path in path_list:

        new_div = ' <div class="nf-item drawing"> \
                        <div class="item-box"> \
                            <a target="_blank" href="' + path + '">\
                                <img alt="1" src="' + path + '" class="item-container"> \
                                <div class="item-mask">\
                                    <div class="item-caption">\
                                        <h5 class="white"></h5>\
                                        <p class="white"></p>\
                                    </div>\
                                </div>\
                            </a>\
                        </div>\
                    </div>'
        html_div_list.append(new_div)



    # photography
    directory = os.fsencode("/Users/austinhunt/Desktop/TheMotherload/huntaj_stu/main/static/main/img/photography")

    path_list = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        filename = "huntaj_stu/main/static/main/img/photography/" + filename

        path_list.append(filename)

    for path in path_list:
        new_div = ' <div class="nf-item photo"> \
                            <div class="item-box"> \
                                <a target="_blank" href="' + path + '">\
                                    <img alt="1" src="' + path + '" class="item-container"> \
                                    <div class="item-mask">\
                                        <div class="item-caption">\
                                            <h5 class="white"></h5>\
                                            <p class="white"></p>\
                                        </div>\
                                    </div>\
                                </a>\
                            </div>\
                        </div>'
        html_div_list.append(new_div)

    f = open('/Users/austinhunt/Desktop/new_divs.txt', 'a')

    shuffle(html_div_list)
    for div in html_div_list:
        f.write("\n\n\n" + div + "\n\n\n")
    f.close()



automate_portfolio()
