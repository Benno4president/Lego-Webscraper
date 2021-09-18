import concurrent.futures
import time

from LegoModel import Theme, Legoset
from ScraperLib import *


def ScrapeLegoSet(mo):
    # print("#", end="")
    ProgressBar.update()
    # Price
    model_soup = requestSoup(mo.link)

    # big_box
    nametemp = findElmt(model_soup, 'div', 'class', 'ProductOverviewstyles__ProductOverviewRow-sc-1a1az6h-1 hblOYO')
    mo.name = findElmt(nametemp, 'span', 'class', 'Markup__StyledMarkup-ar1l9g-0 hlipzx', get_text=True)

    # temp_link_soup = findAllElmt(model_soup, 'ol', 'class', 'breadcrumbsstyles__Wrapper-sc-15z7ihn-0 fEVsMb ProductDetailsPagestyles__Breadcrumbs-sc-1waehzg-0 jHjxNV')
    # mo.link = \
    # findAllElmt(temp_link_soup[0], 'source', get_item='srcset')
    # print(mo.link)

    big_boxtemp = findElmt(model_soup, 'div', 'class', 'ProductDetailsstyles__AttributesWrapper-sc-16lgx7x-1 dxRXjG')
    small_boxtemp = findAllElmt(big_boxtemp, 'span', 'class',
                                'Text__BaseText-sc-178efqu-0 cMNVBC ProductDetailsstyles__ProductAttributeValue-sc-16lgx7x-6 iLLHZh')
    mo.age = int(small_boxtemp[0].text.split('+')[0].split('-')[0].split('½')[0])
    mo.amount_bricks = int(small_boxtemp[1].text)
    if len(small_boxtemp) <= 3:
        mo.product_number = 00000
    else:
        mo.product_number = int(small_boxtemp[3].text)
    mo.price = int(small_boxtemp[2].text)
    big_starboxtemp = findElmt(model_soup, 'div', 'class',
                               'Spacing-iay53v-0 ProductReviewsOverviewstyles__BreakdownWrapper-echww5-2 jrAhXd')
    if big_starboxtemp is None:
        mo.rating_amount = 00000
        mo.rating_worth = 00000
        mo.rating_fun = 00000
    else:
        mo.rating_amount = findElmt(big_starboxtemp, 'span', 'class',
                                    'RatingBarstyles__RatingDisplay-sc-11ujyfe-0 iDkflT', get_text=True)

        starboxtemp = findAllElmt(big_starboxtemp, 'div', 'class',
                                  'RatingBarstyles__RatingContainer-sc-11ujyfe-2 fgbdIf', get_item='title')
        mo.rating_fun = float(starboxtemp[0])
        mo.rating_worth = float(starboxtemp[1])

        # mo.print()

    return mo
    # print(len(themes),len(legosets))


def LegoDotComScraper(link, nrofthemes=50000):
    soup = requestSoup(link)
    core_link: str = 'https://www.lego.com'
    themes: list[Theme] = []
    legosets = []
    theme_souplist = findAllElmt(soup, 'div', 'class', 'CategoryLeafstyles__Details-is33yg-4 fXkPfj')
    for th in theme_souplist:
        if len(themes) == nrofthemes:
            break
        new_theme = Theme()
        new_theme.name = findElmt(th, 'span', 'class', 'Markup__StyledMarkup-ar1l9g-0 hlipzx', get_text=True)
        new_theme.link = core_link + findElmt(th, 'a', 'class', 'CategoryLeafstyles__DetailsLink-is33yg-13 grChXe',
                                              get_item='href')
        themes.append(new_theme)

    ProgressBar.process_length = len(themes)
    ProgressBar.process_pretext = 'Pulling sets from themes:'
    ProgressBar.start()
    for ls in themes:
        set_soup = requestSoup(ls.link)
        legosets_box_soup = findAllElmt(set_soup, 'div', 'class',
                                        'ProductLeafSharedstyles__Wrapper-sc-1epu2xb-0 ProductLeafListingstyles__Wrapper-sc-19n1otk-0 hQdRgg')
        # print(ls.name, ls.link)
        legoset_href_list: list[str] = []

        for sp in legosets_box_soup:
            lego_link = findElmt(sp, 'a', 'class', 'ProductImagestyles__ProductImageLink-sc-1sgp7uc-0 dwJQhm',
                                 get_item='href')
            legoset_href_list.append(lego_link)

        for i in legoset_href_list:
            new_legoset = Legoset()
            new_legoset.link = core_link + i
            legosets.append(new_legoset)
            # print(new_legoset.link)
        ProgressBar.update()

    ProgressBar.process_length = len(legosets)
    ProgressBar.process_pretext = 'Pulling info from sets:'
    ProgressBar.start()
    # ## single threading
    for i in legosets:
        ScrapeLegoSet(i)

    # ## multi threading
    """
    amount_of_threads = 5
    list_split_by_threads = list(divide_chunks(legosets, amount_of_threads))
    with concurrent.futures.ThreadPoolExecutor(max_workers=amount_of_threads) as executor:
        futures = {(executor.submit(ScrapeLegoSet, sub_list) for sub_list in list_split_by_threads)}
        futures, _ = concurrent.futures.wait(futures)
        for future in futures:
            result = future.result()
            print(result.print())
    legosets_ = mergeListOfLists(list_split_by_threads)
    """

    return legosets


def main():
    legodotcom = 'https://www.lego.com/da-dk/themes'

    t0 = time.time()
    lego_setliste = LegoDotComScraper(legodotcom)
    # save_objects_to_path(lego_setliste, "pickle.rick")
    print(ANSI_RAINBOW("   GHETTO SHIT"))
    t1 = time.time()
    print(f"It took {ANSI_YELLOW(t1 - t0)} seconds to download to save {ANSI_GREEN(len(lego_setliste))} legoset models.")
    print('average time pr set:', (t1 - t0)/len(lego_setliste))


if __name__ == '__main__':
    main()

