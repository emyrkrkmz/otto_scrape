import scrapy
import json
from scrapy_playwright.page import PageMethod
from otto_scrape.items import Product


class OttoLittleSpySpider(scrapy.Spider):
    name = "otto_little_spy"
    
    # def start_requests(self):
    #     with open('output.json', 'r') as file:
    #         data = json.load(file)
            
    #     for entry in data:
    #         url = entry.get("url")
    #         if url:
    #             yield scrapy.Request(url=url, callback=self.parse, meta=dict(
    #                     playwright=True,
    #                     playwright_include_page=True,
    #                     playwright_page_methods=[
    #                         PageMethod("wait_element", '//span[contains(@class,"retailer-name")]'),
    #                         PageMethod("click", '//span[contains(@class,"retailer-name")]'),
    #                         PageMethod("wait_element", '//div[contains(@class, "pl_table-view--full-bleed")]/div[8]'),
    #                         PageMethod("click", '//div[contains(@class, "pl_table-view--full-bleed")]/div[8]')
    #                     ],
    #                 ))
    
    
    def start_requests(self):
        urls = [
        "https://www.otto.de/p/kunstbaum-distanzabhaenger-fitu-pendelleuchte-schwarz-deckenmontage-slv-weiteres-zubehoer-CS0NBQ00G/#variationId=S0Q3F0MU7E6J",
        "https://www.otto.de/p/nordesign-duschablage-seifenspender-set-mit-selbstklebender-metall-wandhalterung-6-tlg-6-tlg-mit-hochwertigen-pumpspendern-S06BQ03D/#variationId=S06BQ03DZSZU",
        "https://www.otto.de/p/trizeratop-zulaufschlauch-anschlussschlauch-inneng-ausseng-3-8-m10x1-600mm-zubehoer-fuer-bade-kueche-S0LAO0DE/#variationId=S0LAO0DEFVYV",
        "https://www.otto.de/p/nordesign-duschablage-seifenspender-set-mit-selbstklebender-metall-wandhalterung-6-tlg-6-tlg-mit-hochwertigen-pumpspendern-S06BQ03D/#variationId=S06BQ03DZSZU",
        "https://www.otto.de/p/kunstbaum-abhaengeset-medo-60-led-in-silbergrau-slv-weiteres-zubehoer-CS0NBQ056/#variationId=S0Q3F0Q40CMB",
        "https://www.otto.de/p/elegear-duschablage-duschkorb-edelstahl-ohne-bohren-duschablage-mit-haken-dusch-ablage-2-tlg-badregal-zum-haengen-10kg-max-duschzubehoer-badezimmerorganizer-S0P0V0AI/#variationId=S0P0V0AIKSEG",
        "https://www.otto.de/p/trizeratop-zulaufschlauch-anschlussschlauch-inneng-ausseng-3-8-m10x1-300mm-zubehoer-fuer-bade-kueche-S0LAO0EX/#variationId=S0LAO0EXQUUE",
        "https://www.otto.de/p/elegear-duschablage-duschkorb-edelstahl-ohne-bohren-duschablage-mit-haken-dusch-ablage-2-tlg-badregal-zum-haengen-10kg-max-duschzubehoer-badezimmerorganizer-S0P0V0AI/#variationId=S0P0V0AIKSEG",
        "https://www.otto.de/p/kunstbaum-mix-match-tischleuchtenfuss-single-fenda-max-60-w-schwarz-slv-hoehe-43-5-cm-weiteres-zubehoer-CS0NBQ0DB/#variationId=S0R3F0ZAQJ6N",
        "https://www.otto.de/p/kunstbaum-cover-alwaid-i-in-verkehrsweiss-deko-light-hoehe-2-cm-weiteres-zubehoer-S095V0YY/#variationId=S095V0YYUPY5",
        "https://www.otto.de/p/trizeratop-zulaufschlauch-anschlussschlauch-inneng-ausseng-3-8-m10x1-800mm-zubehoer-fuer-bade-kueche-S0LAO0KK/#variationId=S0LAO0KKZCO9",
        "https://www.otto.de/p/kunstbaum-abstandshalter-set-tenseo-elektrisch-in-schwarz-slv-weiteres-zubehoer-S0H3F0CK/#variationId=S0H3F0CKJQHH",
        "https://www.otto.de/p/hytireby-duschablage-duschablage-ohne-bohren-badezimmer-regal-mit-seifenhalter-und-haken-3-tlg-schwarz-duschablage-duschkorb-fuer-bad-kueche-S0H7U0C0/#variationId=S0H7U0C014I3",
        "https://www.otto.de/p/casa-padrino-wannenarmatur-luxus-jugendstil-einhebel-badewannenarmatur-14-8-x-h-12-8-cm-verschiedene-farben-eleganter-wasserhahn-mit-kristallglas-bad-zubehoer-S0P5G0F9/#variationId=S0P5G0F9EWEL",
        "https://www.otto.de/p/kunstbaum-mix-match-deckenrosette-fenda-max-60-w-schwarz-slv-hoehe-9-5-cm-weiteres-zubehoer-CS0NBQ0E6/#variationId=S0O3F0CMMAD7",
        "https://www.otto.de/p/kunstbaum-ersatz-akku-fuer-pina-pro-push-up-home-poldina-l-zafferano-weiteres-zubehoer-S097Z0KZ/#variationId=S097Z0KZKX4V",
        "https://www.otto.de/p/kunstbaum-mix-match-lampenschirm-lalu-plate-15-in-schwarz-matt-und-bronze-matt-slv-hoehe-1-5-cm-weiteres-zubehoer-CS0RBQ0AZ/#variationId=S0Y9V0GTTAU5",
        "https://www.otto.de/p/kunstbaum-zierring-mit-strukturiertem-diffusor-fuer-enola_c-serie-rund-weiss-slv-weiteres-zubehoer-S0H3F0G4/#variationId=S0H3F0G4M0ME",
        "https://www.otto.de/p/refined-living-duschregal-2-stueck-eckregal-ohne-bohren-aus-rostfreiem-aluminium-fuer-die-dusche-badezimmer-duschablage-selbstklebendes-oder-bohren-2-tlg-mit-4-klebeflaechen-und-4-haken-fuer-baeder-kuechen-duschgel-grau-schwarz-S0JBH03O/#variationId=S0JBH03OTYE3",
        "https://www.otto.de/p/casa-padrino-waschtischarmatur-luxus-bad-zubehoer-jugendstil-retro-bidet-armatur-einlochbatterie-altgold-bronze-serie-milano-made-in-italy-S0P5G0FC/#variationId=S0P5G0FCL8YP",
        "https://www.otto.de/p/kunstbaum-mix-match-tischleuchtenfuss-single-fenda-max-60-w-gebuerstetem-metall-slv-hoehe-43-5-cm-weiteres-zubehoer-CS0NBQ0EP/#variationId=S0P3J0TLMXRP",
        "https://www.otto.de/p/kunstbaum-deckeneinbauring-new-tria-in-schwarz-eckig-90mm-slv-hoehe-2-6-cm-weiteres-zubehoer-S099V012/#variationId=S099V012HS7F",
        "https://www.otto.de/p/spirella-badaccessoires-sets-tube-matt-zubehoer-set-aus-hochwertiger-keramik-schwarz-elegante-matt-optik-5-tlg-bestehend-aus-wc-buerste-seifenspender-2x-zahnputzbecher-seifenschale-S070T05F/#variationId=S070T05F3F39",
        "https://www.otto.de/p/kunstbaum-anela-reflektor-28-gold-slv-hoehe-10-5-cm-weiteres-zubehoer-S0H3F0HD/#variationId=S0H3F0HD756G",
        "https://www.otto.de/p/abakuhaus-badorganizer-anti-rutsch-stoffabdeckung-fuer-waschmaschine-und-trockner-mode-kleiden-und-zubehoer-motiv-S0Y1Y01G/#variationId=S0Y1Y01G8ZWN",
        "https://www.otto.de/p/casa-padrino-wannenarmatur-luxus-badewannenarmatur-silber-freistehende-messing-badewannen-armatur-mit-handbrause-luxus-badezimmer-zubehoer-S0P5G0FE/#variationId=S0P5G0FEKHA0",
        "https://www.otto.de/p/koenig-design-handyhuelle-apple-iphone-12-pro-max-schutzhuelle-fuer-apple-iphone-12-pro-max-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S0Z270HG/#variationId=S0Z270HGQ6W6",
        "https://www.otto.de/p/refined-living-duschregal-2-stueck-eckregal-ohne-bohren-aus-rostfreiem-aluminium-fuer-die-dusche-badezimmer-duschablage-selbstklebendes-oder-bohren-2-tlg-mit-4-klebeflaechen-und-4-haken-fuer-baeder-kuechen-duschgel-grau-schwarz-S0JBH03O/#variationId=S0JBH03OTYE3",
        "https://www.otto.de/p/kunstbaum-mix-match-deckenrosette-fenda-max-60-w-weiss-slv-hoehe-9-5-cm-weiteres-zubehoer-CS0NBQ0FL/#variationId=S0O3F06WHI2O",
        "https://www.otto.de/p/kunstbaum-deckeneinbauring-new-tria-in-aluminium-eckig-110mm-slv-hoehe-2-6-cm-weiteres-zubehoer-S099V0IF/#variationId=S099V0IFDPJZ",
        "https://www.otto.de/p/kunstbaum-funktioneller-distanzhalter-fuer-wandleuchten-aus-kunststoff-in-schwarz-konstsmide-hoehe-10-5-cm-weiteres-zubehoer-CS04B20YE/#variationId=S0Q3F0Z2E7IV",
        "https://www.otto.de/p/kunstbaum-diffusor-numinos-s-in-schwarz-wabe-slv-hoehe-0-4-cm-weiteres-zubehoer-S0H3F0IB/#variationId=S0H3F0IB3X0K",
        "https://www.otto.de/p/damixa-unterlegscheibe-bad-zubehoer-48424-00-CS0966047/#variationId=S0966047RQNW",
        "https://www.otto.de/p/casa-padrino-wannenarmatur-luxus-bad-zubehoer-jugendstil-retro-unterputz-wannenbatterie-mit-schlauch-handbrause-und-wandhalter-armatur-fuer-badewanne-chrom-serie-milano-made-in-italy-S0P5G0FF/#variationId=S0P5G0FFO8VY",
        "https://www.otto.de/p/koenig-design-handyhuelle-apple-iphone-12-mini-schutzhuelle-fuer-apple-iphone-12-mini-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S0Z270HH/#variationId=S0Z270HH30GC",
        "https://www.otto.de/p/houseproud-badaccessoire-set-ceramic-silk-badset-S0L3J0ZB/#variationId=S0L3J0ZBVAZM",
        "https://www.otto.de/p/kunstbaum-rahmen-aufputzmontage-silbergrau-slv-hoehe-11-6-cm-weiteres-zubehoer-CS0NBQ0NP/#variationId=S0R3F0GBK2XT",
        "https://www.otto.de/p/kunstbaum-deckeneinbauring-new-tria-in-aluminium-eckig-slv-hoehe-2-6-cm-weiteres-zubehoer-S099V0JA/#variationId=S099V0JA8QC8",
        "https://www.otto.de/p/wishdor-puppenhaus-puppenhaus-spielset-hoelzernes-mit-moebeln-und-zubehoer-puppenhausmoebel-mit-schlafzimmer-wohnzimmer-esszimmer-badezimmer-60-00-cm-x24-00-cm-x-70-00-cm-lxwxh-pink-mit-zubehoer-fuer-puppen-zwischen-7-12-cm-suesses-grosses-traumhaus-3plus-S0V6F02T/#variationId=S0V6F02TR76S",
        "https://www.otto.de/p/kunstbaum-reflektor-fuer-supros-regular-inkl-glas-und-fixierring-40-slv-hoehe-4-9-cm-weiteres-zubehoer-S0H3F0J5/#variationId=S0H3F0J5CRGA",
        "https://www.otto.de/p/sanixa-regenduschkopf-wellness-dusche-bad-zubehoer-brausekopf-kopfbrause-duschbrause-antikalk-duesen-regenbrause-quadratisch-20-cm-regendusche-duschkopf-regen-S022R083/#variationId=S022R0835MIR",
        "https://www.otto.de/p/casa-padrino-duscharmatur-luxus-bad-zubehoer-jugendstil-retro-unterputz-duschen-einhebelmischer-mit-druecktaste-chrom-serie-milano-made-in-italy-S0P5G0FG/#variationId=S0P5G0FGF5HH",
        "https://www.otto.de/p/koenig-design-handyhuelle-huawei-y5p-schutzhuelle-fuer-huawei-y5p-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S0Z270HI/#variationId=S0Z270HIMIKR",
        "https://www.otto.de/p/montegoni-duschablage-badezimmer-regal-keine-bohr-regale-wand-halterung-duschkoerbe-duschablagen-badezimmer-regal-selbstklebendes-oder-stanzen-badezimmerzubehoer-S0YBR04J/#variationId=S0YBR04JZB4C",
        "https://www.otto.de/p/kunstbaum-fitu-rosette-lang-in-schwarz-3-flammig-slv-hoehe-5-cm-weiteres-zubehoer-CS0O3F02Y/#variationId=S0O3F02YUST9",
        "https://www.otto.de/p/kunstbaum-dekorativer-ring-cyft-in-schwarz-matt-slv-hoehe-2-4-cm-weiteres-zubehoer-S09BM0KS/#variationId=S09BM0KSRJ6C",
        "https://www.otto.de/p/kunstbaum-play-5m-verlaengerungskabel-philips-hue-weiteres-zubehoer-CS053L073/#variationId=S053L073WLPM",
        "https://www.otto.de/p/kunstbaum-montagegehaeuse-dasar-premium-in-schwarz-309mm-slv-hoehe-17-6-cm-weiteres-zubehoer-S0H3F0JJ/#variationId=S0H3F0JJUNAC",
        "https://www.otto.de/p/dm-handel-wandhalter-waschtischhalterung-winkel-wandhalter-waschtischhalterung-handtuchhalter-regalwinkel-wandregaltraeger-schwerlasttraeger-stabil-S079H0A5/#variationId=S079H0A5SCJT",
        "https://www.otto.de/p/casa-padrino-wannenarmatur-luxus-jugendstil-aufputz-badewannenarmatur-silber-weiss-h-46-95-cm-nostalgische-messing-badewannen-armatur-mit-handbrause-nostalgisches-badezimmer-zubehoer-S0P5G0FL/#variationId=S0P5G0FL64FB",
        "https://www.otto.de/p/koenig-design-handyhuelle-huawei-p8-lite-2017-schutzhuelle-fuer-huawei-p8-lite-2017-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S0Z270HJ/#variationId=S0Z270HJ1Z6Q",
        "https://www.otto.de/p/spirella-badaccessoires-sets-accessoire-set-sydney-zubehoer-set-aus-hochwertigem-acryl-5-tlg-bestehend-aus-wc-buerste-kosmetikeimer-5l-seifenspender-200-ml-zahnputzbecher-seifenschale-robust-langlebig-stylisher-look-glaenzend-sand-beige-komplett-set-badezimmerzubehoer-5-tlg-5-tlg-acryl-stylisher-look-sand-beige-glaenzend-S000R0H1/#variationId=S000R0H13ZAB",
        "https://www.otto.de/p/kunstbaum-deckenrosette-fuer-photonia-outdoor-pendelleuchte-anthrazit-ip44-slv-weiteres-zubehoer-CS0O3F0EF/#variationId=S0O3F0EFWJYI",
        "https://www.otto.de/p/kunstbaum-adapter-fuer-einbaudurchmesser-von-75-120-mm-auf-68-70-mm-weiss-matt-paulmann-hoehe-1-cm-weiteres-zubehoer-S0A1P0ID/#variationId=S0A1P0IDD6U6",
        "https://www.otto.de/p/lb-h-f-lilienburg-wandhalter-haken-halter-bad-badezimmer-handtuch-handtuchhaken-anker-shabby-vintage-maritime-deko-badtuchhalter-geschirrtuchhalter-geschirrtuchhaken-wandhaken-geschirrtuch-kuechentuch-kuechenhaken-badhaken-landhausstil-rustikal-retro-wandmontage-badezimmer-antik-nostalgie-barock-landhaus-metall-gusseisen-handtuchhalter-handtuchring-handtuchstange-handtuchhalterung-kueche-S0A6Q08S/#variationId=S0A6Q08SCVZL",
        "https://www.otto.de/p/kunstbaum-abdeckung-big-plot-in-anthrazit-2-auslaesse-slv-hoehe-2-cm-weiteres-zubehoer-S0H3F0LO/#variationId=S0H3F0LOP0Q2",
        "https://www.otto.de/p/sanixa-seifenschale-hochwertige-badaccessoires-serie-oslo-aluminium-handtuchstange-60cm-rostfrei-badezimmer-wand-handtuchhalter-handtuch-halter-zubehoer-S0D2M0MD/#variationId=S0D2M0MDR3UZ",
        "https://www.otto.de/p/casa-padrino-waschtischarmatur-luxus-bad-zubehoer-jugendstil-retro-waschtisch-armatur-einlochbatterie-altgold-bronze-serie-milano-made-in-italy-S0P5G0FM/#variationId=S0P5G0FMPHUS",
        "https://www.otto.de/p/koenig-design-handyhuelle-apple-iphone-13-mini-schutzhuelle-fuer-apple-iphone-13-mini-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S0Z270HK/#variationId=S0Z270HKR4W6",
        "https://www.otto.de/p/aoucheni-handtuchhalter-ohne-bohren-badetuchstange-40cm-edelstahl-badezimmer-zubehoer-CS0GC20WC/#variationId=S0GC20WC7AN0",
        "https://www.otto.de/p/kunstbaum-fitu-rosette-lang-in-weiss-3-flammig-slv-hoehe-5-cm-weiteres-zubehoer-CS0OBQ0HC/#variationId=S0Q3F0XKHMN7",
        "https://www.otto.de/p/kunstbaum-edelstahl-schraubenset-m8-slv-weiteres-zubehoer-S0A1P0OS/#variationId=S0A1P0OSQGFG",
        "https://www.otto.de/p/bremermann-badaccessoire-set-badezimmer-set-3-tlg-bambus-badezimmer-zubehoer-set-S012U0CD/#variationId=S012U0CDV7AN",
        "https://www.otto.de/p/kunstbaum-befestigungsclips-fuer-unterbauleuchte-mia-deko-light-weiteres-zubehoer-S0H3F0M0/#variationId=S0H3F0M0IH4R",
        "https://www.otto.de/p/m2-tec-2000a-starthilfekabel-federklemme-federklemme-3-cm-geeignet-fuer-alle-gaengigen-fahrzeuge-fuer-den-staendigen-gebrauch-im-aussenbereich-geeignet-S0D480PG/#variationId=S0D480PGDUSH",
        "https://www.otto.de/p/casa-padrino-waschtischarmatur-luxus-waschtischarmatur-mit-swarovski-kristallglas-silber-13-5-x-h-16-5-cm-luxus-bad-zubehoer-made-in-italy-S0P5G0FP/#variationId=S0P5G0FP2BTW",
        "https://www.otto.de/p/koenig-design-handyhuelle-huawei-y550-schutzhuelle-fuer-huawei-y550-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S0Z270HL/#variationId=S0Z270HL723S",
        "https://www.otto.de/p/iceagle-handtuchhalter-handtuchhalter-selbstklebend-ohne-bohren-40-cm-edelstahl-badezimmer-zubehoer-CS0GC20WY/#variationId=S0GC20WY71RG",
        "https://www.otto.de/p/kunstbaum-fitu-rosette-lang-in-schwarz-5-flammig-slv-hoehe-5-cm-weiteres-zubehoer-CS0OBQ0IF/#variationId=S0Q3F0UTHU0P",
        "https://www.otto.de/p/kunstbaum-cover-alwaid-iii-in-aluminium-deko-light-hoehe-2-cm-weiteres-zubehoer-S0A5V0B2/#variationId=S0A5V0B2RQOF",
        "https://www.otto.de/p/koenig-design-handyhuelle-xiaomi-redmi-9at-schutzhuelle-fuer-xiaomi-redmi-9at-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S05290CZ/#variationId=S05290CZVZ8G",
        "https://www.otto.de/p/kunstbaum-deco-kappe-special-line-cap-rund-fuer-set-special-line-ip65-led-paulmann-hoehe-1-7-cm-weiteres-zubehoer-S0H9A0PM/#variationId=S0H9A0PMF9WV",
        "https://www.otto.de/p/bagnoxx-seifenspender-seifenschale-seifenablage-edelstahl-1-tlg-badezimmer-zubehoer-ablageschale-fuer-seife-einfache-reinigung-S0E2703D/#variationId=S0E2703D7MCJ",
        "https://www.otto.de/p/casa-padrino-waschtischarmatur-jugendstil-retro-waschtisch-waschbecken-armatur-silber-h-21-cm-nostalgisches-bad-zubehoer-S0P5G0FR/#variationId=S0P5G0FR81BR",
        "https://www.otto.de/p/koenig-design-handyhuelle-apple-iphone-13-pro-schutzhuelle-fuer-apple-iphone-13-pro-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S0Z270HM/#variationId=S0Z270HMLJJ9",
        "https://www.otto.de/p/spirella-badaccessoires-sets-akira-badezimmer-zubehoer-set-2-tlg-bestehend-aus-kosmetikeimer-5l-treteimer-mit-softclose-absenkautomatik-und-wc-garnitur-mit-hygienischem-innenbehaelter-und-deckel-stahl-matt-satiniert-angesagte-trendfarben-dunkelgruen-kombi-set-S0G1S0EI/#variationId=S0G1S0EIIDBU",
        "https://www.otto.de/p/kunstbaum-eckverbinder-border-clever-connect-12v-in-weiss-matt-paulmann-weiteres-zubehoer-CS0P6H0W8/#variationId=S0S990ZK7WC5",
        "https://www.otto.de/p/kunstbaum-cover-alwaid-v-in-schwarz-deko-light-hoehe-2-1-cm-weiteres-zubehoer-S0A5V0PV/#variationId=S0A5V0PV5UH8",
        "https://www.otto.de/p/bada-bing-badaccessoire-set-bad-ausstattung-badezimmerdeko-zubehoer-keramik-weiss-mit-sternen-hochwertige-badgarnitur-komplett-set-4-tlg-4er-set-seifenspender-zahnputzbecher-seifenschale-zahnbuerstenhalter-S0A990XQ/#variationId=S0A990XQLUHX",
        "https://www.otto.de/p/kunstbaum-deckeneinbauring-new-tria-in-aluminium-rund-slv-hoehe-2-6-cm-weiteres-zubehoer-S0H9V086/#variationId=S0H9V086VHIW",
        "https://www.otto.de/p/jt-berlin-organizer-kreuzberg-echtleder-taschenleerer-fuer-buero-und-zu-hause-18x13cm-schreibtischbox-aufbewahrungsbox-fuer-schluessel-und-kleinteile-aufklappbar-schwarz-S0F0K0G9/#variationId=S0F0K0G9NKKH",
        "https://www.otto.de/p/casa-padrino-wannenarmatur-luxus-badewannenarmatur-gold-messing-badewannen-armatur-mit-handbrause-luxus-badezimmer-zubehoer-S0P5G0FS/#variationId=S0P5G0FSK412",
        "https://www.otto.de/p/koenig-design-handyhuelle-huawei-y625-schutzhuelle-fuer-huawei-y625-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S0Z270HN/#variationId=S0Z270HNYSNK",
        "https://www.otto.de/p/hytireby-duschablage-eck-duschregal-ohne-bohren-aufbewahrung-badezimmer-zubehoer-2-tlg-duschregal-rostfrei-aluminium-weiss-S08BI0UP/#variationId=S08BI0UPUDA4",
        "https://www.otto.de/p/kunstbaum-abstandshalter-in-anthrazit-slv-weiteres-zubehoer-CS0PBQ00A/#variationId=S0W3K0UYHIQT",
        "https://www.otto.de/p/elegear-duschkorb-duschablage-edelstahl-duschregal-ohne-bohren-mit-haken-set-2-tlg-duschablage-selbstklebendes-mit-3-klebeflaechen-fuer-baeder-kuechen-S041D0JN/#variationId=S041D0JNMI8G",
        "https://www.otto.de/p/kaminbau-mierzwa-echtfeuer-dekokamin-lukas-premium-royal-inkl-komplettem-zubehoer-sicherheitsglas-gelkamin-ethanolkamin-bodenkamin-kaminofen-S0H5Q09A/#variationId=S0H5Q09AR93I",
        "https://www.otto.de/p/elegear-duschkorb-duschablage-edelstahl-duschregal-ohne-bohren-mit-haken-set-2-tlg-duschablage-selbstklebendes-mit-3-klebeflaechen-fuer-baeder-kuechen-S041D0JN/#variationId=S041D0JNMI8G",
        "https://www.otto.de/p/macosa-home-wandhalter-wand-haken-im-vintage-stil-retro-antik-metall-braun-garderobenhaken-kleiderhaken-handtuchhaken-metallhaken-flur-garderobe-S0G3B0A3/#variationId=S0G3B0A3YOG6",
        "https://www.otto.de/p/casa-padrino-waschtischarmatur-luxus-bad-zubehoer-jugendstil-retro-bidet-dreilochbatterie-chrom-serie-milano-made-in-italy-S0P5G0FU/#variationId=S0P5G0FUIE0R",
        "https://www.otto.de/p/koenig-design-handyhuelle-huawei-y635-schutzhuelle-fuer-huawei-y635-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S0Z270HO/#variationId=S0Z270HO70YI",
        "https://www.otto.de/p/rutaqian-badaccessoire-set-7-teiliges-kunststoff-badezimmer-zubehoer-set-mit-seifenschale-seifenspender-nachfuellbar-seifenspender-nachfuellbar-zahnbuerstenhalter-set-mit-bambusdeckel-fuer-boho-theke-S0QAR08B/#variationId=S0QAR08BTVVS",
        "https://www.otto.de/p/kunstbaum-mix-match-lampenschirm-lalu-tetra-36-in-weiss-matt-und-gold-matt-slv-hoehe-8-9-cm-weiteres-zubehoer-CS0RBQ078/#variationId=S0Z9V0YQMK8T",
        "https://www.otto.de/p/navaris-badezimmer-set-bambus-4-teilig-zahnputzbecher-seifenspender-becher-ablage-4-st-S001J0XB/#variationId=S001J0XB1HOU",
        "https://www.otto.de/p/bremermann-badaccessoire-set-badezimmer-set-zubehoer-set-4-tlg-kunststoff-savona-grau-S0T9Z0OC/#variationId=S0T9Z0OCVFE6",
        "https://www.otto.de/p/navaris-badezimmer-set-badezimmer-set-holz-3-teilig-badzubehoer-aus-holz-1-st-S09350WW/#variationId=S09350WW0WT1",
        "https://www.otto.de/p/trizeratop-zulaufschlauch-anschlussschlauch-innengewinde-1-2-3-8-800mm-zubehoer-fuer-bade-kueche-S0LAO09C/#variationId=S0LAO09CNLXC",
        "https://www.otto.de/p/casa-padrino-wannenarmatur-luxus-badewannen-armatur-mit-swarovski-kristallglas-gold-h-7-cm-einlochbatterie-mit-ablaufgarnitur-luxus-bad-zubehoer-made-in-italy-S0P5G0FW/#variationId=S0P5G0FWFLAC",
        "https://www.otto.de/p/koenig-design-handyhuelle-huawei-y6p-schutzhuelle-fuer-huawei-y6p-motiv-handy-huelle-silikon-tasche-case-cover-dont-touch-my-phone-baer-schwarz-S0Z270HP/#variationId=S0Z270HPQ0J4",
        "https://www.otto.de/p/msv-badaccessoires-sets-hannah-zubehoer-set-aus-hochwertigem-kunststoff-6-tlg-bestehend-aus-kosmetikeimer-wc-buerste-seifenspender-zahnputzbecher-zahnbuerstenhalter-seifenschale-elegante-matt-optik-schwarz-komplett-set-badezimmerzubehoer-6-tlg-in-edler-matt-optik-schwarz-S0K0I01B/#variationId=S0K0I01B1H5P",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        PageMethod("wait_element", '//span[contains(@class, "retailer-name")]'),
                        PageMethod("click", '//span[contains(@class, "retailer-name")]'),
                        PageMethod("wait_element", '//div[contains(@class, "pl_table-view--full-bleed")]/div[8]'),
                        PageMethod("click", '//div[contains(@class, "pl_table-view--full-bleed")]/div[8]')
                    ],
                ))

    async def parse(self, response):
        page = response.meta["playwright_page"]
        product = Product()
        
        product["Url"] = response.url
        product["Company_Name"] = response.xpath('//h1[@class = "pd_header__headline"]/text()').get()
        product["Address"] = response.xpath('//div[contains(@class, "pl_table-view--full-bleed")]/div[8]/div/div[2]/p[2]/text()').get()
        product["Phone_Number"] = response.xpath('//div[contains(@class, "pl_table-view--full-bleed")]/div[8]/div/div[2]/p[3]/a[1]/text()').get()
        product["Mail"] = response.xpath('//div[contains(@class, "pl_table-view--full-bleed")]/div[8]/div/div[2]/p[3]/a[2]/text()').get()
        product["Product_Name"] = response.xpath('//h1[@data-qa="variationName"]/div[2]/text()').get()
        
        yield product
        
        await page.close()
