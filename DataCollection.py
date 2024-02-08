from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
from lxml import etree
import json
import pandas as pd

import concurrent.futures
import time

sub_d_links = """/pl/Accessible-bathroom-Accessible-home/37721669146437
/pl/Accessible-bedroom-Accessible-home/4294644781
/pl/Accessible-entry-home-Accessible-home/37721669146444
/pl/Accessible-kitchen-Accessible-home/1111913019980
/pl/Daily-assistance-Accessible-home/4294644797
/pl/Injury-relief-physical-therapy-Accessible-home/4294644776
/pl/Wheelchairs-mobility-aids-Accessible-home/4294644793
/pl/Livestock-supplies-Animal-pet-care/1697941494
/pl/Pet-beds-houses-furniture-Animal-pet-care/2544332199
/pl/Pet-cleaning-waste-supplies-Animal-pet-care/2318112555
/pl/Pet-clippers-scissors-brushes-Animal-pet-care/3121493845732
/pl/Pet-clothing-accessories-Animal-pet-care/2921724317701
/pl/Pet-doors-gates-Animal-pet-care/4294610550
/pl/Pet-feeding-supplies-Animal-pet-care/2510803352
/pl/Pet-fencing-training-Animal-pet-care/3583519698
/pl/Pet-grooming-health-Animal-pet-care/4294610546
/pl/Pet-kennels-crates-Animal-pet-care/778128516
/pl/Pet-leashes-collars-harnesses-Animal-pet-care/4233103602
/pl/Pet-toys-treats-Animal-pet-care/4294610530
/pl/Pet-travel-transportation-Animal-pet-care/2620088367057
/pl/Pet-vitamins-supplements-Animal-pet-care/2620555201638
/pl/Terrariums-habitats-Animal-pet-care/2311219941942
/c/Appliance-parts-accessories-Appliances
/pl/Beverage-wine-chillers-Appliances/2352008713
/c/Commercial-appliances-Appliances
/c/Cooktops-Appliances
/pl/Crafting-machines-accessories-Appliances/37721669146480
/c/Dishwashers-Appliances
/c/Freezers-ice-makers-Appliances
/pl/Garbage-disposals-Appliances/4294639585
/pl/Kitchen-appliance-packages-Appliances/2020942007672
/pl/Kitchenettes-Appliances/1511792640827
/c/Microwaves-Appliances
/c/Range-hoods-Appliances
/c/Ranges-Appliances
/c/Refrigerators-Appliances
/pl/Sewing-machines-accessories-Appliances/37721669146479
/c/Small-appliances-Appliances
/pl/Trash-compactors-Appliances/4294639583
/c/Vacuum-cleaners-floor-care-Appliances
/c/Wall-ovens-Appliances
/c/Washers-dryers-Appliances
/pl/Water-coolers-pitchers-Appliances/479649473
/pl/Automotive-accessories-Automotive/4294644698
/pl/Automotive-cleaning-Automotive/4294642659
/pl/Automotive-hardware-Automotive/4294644699
/pl/Automotive-maintenance-Automotive/4294542217
/pl/Automotive-tools-Automotive/2772213972
/pl/Car-chargers-jump-starters-Automotive/1442253792
/pl/Cargo-management-Automotive/693130272
/pl/Headlight-bulbs-Automotive/1520967177021
/pl/Shop-tools-equipment-Automotive/761467183
/pl/Towing-equipment-Automotive/2247165814
/c/Bathroom-pedestal-sinks-Bathroom
/c/Bathroom-accessories-hardware-Bathroom
/c/Bathroom-exhaust-fans-parts-Bathroom
/c/Bathroom-faucets-shower-heads-Bathroom
/pl/Bathroom-mirrors-Bathroom/4294737205
/c/Bathroom-safety-Bathroom
/pl/Bathroom-sets-Bathroom/1511187220575
/c/Bathroom-storage-Bathroom
/c/Bathroom-vanities-vanity-tops-Bathroom
/c/Bathtubs-whirlpool-tubs-Bathroom
/pl/Commercial-bathroom-components-Bathroom/4294737179
/pl/Saunas-components-Bathroom/4294736334
/c/Showers-Bathroom
/c/Toilets-toilet-seats-Bathroom
/pl/Boat-dock-ladders-Boating/2248547567
/pl/Boat-anchoring-Boating/2094135052
/pl/Boat-bumpers-buoys-fenders-Boating/2924523892
/pl/Boat-covers-bimini-tops-Boating/46642357
/pl/Boat-electronics-accessories-Boating/240752712
/pl/Boat-fishing-gear-Boating/2665927074
/pl/Boat-fueling-Boating/4093812814
/pl/Boat-hardware-Boating/3865832521
/pl/Boat-lighting-Boating/959070602
/pl/Boat-maintenance-Boating/889299008
/pl/Boat-motor-parts-Boating/728402067
/pl/Boat-pumps-parts-accessories-Boating/4097565281
/pl/Boat-ropes-Boating/698578125
/pl/Boat-switches-knobs-Boating/3136071793
/pl/Books-Books-magazines/4294859000
/pl/Cds-dvds-Books-magazines/4294859004
/pl/Asphalt-repair-tools-Building-supplies/953779431
/c/Ceilings-Building-supplies
/pl/Columns-accessories-Building-supplies/4294425046
/c/Concrete-cement-masonry-Building-supplies
/c/Decking-Building-supplies
/c/Drywall-Building-supplies
/pl/Erosion-control-Building-supplies/4294653871
/c/Fencing-gates-Building-supplies
/pl/Glass-acrylic-Building-supplies/4294713161
/c/Gutters-accessories-Building-supplies
/c/Insulation-accessories-Building-supplies
/pl/Jack-posts-Building-supplies/4294515331
/c/Lumber-composites-Building-supplies
/c/Roofing-Building-supplies
/c/Siding-stone-veneer-Building-supplies
/c/Stairs-railings-Building-supplies
/pl/Ventilation-Building-supplies/4294858190
/pl/Air-fresheners-Cleaning-supplies/4294386817
/pl/All-purpose-cleaners-Cleaning-supplies/4294599038
/pl/Appliance-cleaners-Cleaning-supplies/3108509681
/pl/Bleach-Cleaning-supplies/4294599022
/c/Cleaning-tools-Cleaning-supplies
/pl/Drain-septic-cleaners-Cleaning-supplies/4294598965
/pl/Floor-cleaning-Cleaning-supplies/2719770657
/pl/Glass-window-cleaners-Cleaning-supplies/1920333672
/pl/Household-cleaners-Cleaning-supplies/4294599039
/pl/Household-essentials-Cleaning-supplies/3618734417
/pl/Janitorial-supplies-Cleaning-supplies/3757293999
/pl/Kitchen-bathroom-cleaners-Cleaning-supplies/2532134782
/c/Laundry-supplies-Cleaning-supplies
/pl/Moisture-absorbers-Cleaning-supplies/2428286844
/pl/Mold-removers-Cleaning-supplies/4294729409
/pl/Mold-test-kits-Cleaning-supplies/4294518335
/pl/Outdoor-cleaners-Cleaning-supplies/2033510625
/pl/Trash-recycling-Cleaning-supplies/4294599026
/pl/Activewear-Clothing-work-apparel/37721669146478
/pl/Clothing-Clothing-work-apparel/15211541027983
/pl/Footwear-accessories-Clothing-work-apparel/2711368754867
/pl/Workwear-Clothing-work-apparel/2220616391790
/pl/Beverage-dispensers-Dining-entertaining/4294644703
/pl/Ice-buckets-Dining-entertaining/4294644705
/pl/Party-supplies-Dining-entertaining/4294599098
/pl/Serveware-accessories-Dining-entertaining/4294644701
/pl/Serving-baskets-Dining-entertaining/4294606037
/pl/Serving-trays-caddies-Dining-entertaining/4294644702
/pl/Table-covers-Dining-entertaining/4294606036
/pl/Coffee-Drinks-snacks/4294606035
/pl/Snacks-candy-Drinks-snacks/4294618078
/pl/Soft-drinks-Drinks-snacks/4294633169
/pl/Sports-drinks-Drinks-snacks/4294633168
/pl/Water-Drinks-snacks/4294633170
/c/Batteries-Electrical
/pl/Cable-wire-connectors-Electrical/4294722554
/c/Conduit-conduit-fittings-Electrical
/c/Doorbells-Electrical
/pl/Drones-drone-accessories-Electrical/1236481888
/pl/Electrical-boxes-covers-Electrical/4294653960
/c/Electrical-outlets-plugs-Electrical
/c/Electrical-testers-tools-Electrical
/c/Electrical-wire-cable-Electrical
/c/Electronics-Electrical
/pl/Extension-cords-surge-protectors-Electrical/4294542242
/c/Fire-safety-Electrical
/c/Generators-Electrical
/pl/Light-sockets-adapters-Electrical/4294722560
/c/Light-switches-dimmers-Electrical
/c/Power-distribution-circuit-protection-Electrical
/c/Solar-power-Electrical
/c/Wall-plates-inserts-Electrical
/c/Carpet-carpet-tile-Flooring
/c/Floor-wall-tile-Flooring
/c/Flooring-tools-supplies-Flooring
/pl/Garage-flooring-Flooring/4294642654
/pl/Gym-flooring-Flooring/4294515431
/c/Hardwood-Flooring
/c/Laminate-Flooring
/c/Vinyl-flooring-Flooring
/pl/Air-hockey-tables-accessories-Game-room/4294526354
/pl/Board-games-puzzles-Game-room/4294482072
/pl/Dartboards-accessories-Game-room/4294610493
/pl/Electronic-basketball-games-Game-room/4294610497
/pl/Foosball-tables-Game-room/4294610496
/pl/Multi-game-tables-Game-room/4294610495
/pl/Ping-pong-tables-accessories-Game-room/4294610488
/pl/Playing-cards-Game-room/4294610478
/pl/Pool-tables-accessories-Game-room/4294610484
/pl/Shuffleboard-tables-accessories-Game-room/4294526360
/pl/Video-gaming-accessories-Game-room/1219279601
/pl/Gift-bags-Gift-center/4294415638
/pl/Gift-tags-Gift-center/4294415641
/pl/Greeting-cards-Gift-center/4294415639
/pl/Tissue-paper-Gift-center/4294415642
/pl/Wrapping-paper-Gift-center/4294415637
/c/Glues-Glues-tapes
/c/Tapes-Glues-tapes
/c/Cabinet-hardware-Hardware
/pl/Chains-ropes-tie-downs-Hardware/4294934403
/c/Door-hardware-Hardware
/c/Fasteners-Hardware
/pl/Furniture-hardware-Hardware/4294711128
/pl/Gate-hardware-Hardware/4294856551
/pl/Hardware-lubricants-Hardware/4294607587
/pl/Hooks-Hardware/4294710936
/pl/Keys-key-safes-Hardware/4294711033
/pl/Locks-Hardware/4294400565
/c/Mailboxes-mailbox-posts-Hardware
/pl/Marine-hardware-Hardware/4294710793
/pl/Metal-rods-shapes-sheets-Hardware/2922688282
/pl/Picture-hangers-Hardware/4294710790
/c/Safes-Hardware
/pl/Signs-letters-numbers-Hardware/4294711114
/pl/Specialty-hardware-Hardware/4294711047
/c/Structural-hardware-Hardware
/pl/Window-hardware-Hardware/4294711110
/c/Air-conditioners-fans-Heating-cooling
/c/Air-filters-accessories-Heating-cooling
/c/Air-purifiers-accessories-Heating-cooling
/pl/Boilers-Heating-cooling/1794897186
/c/Fireplaces-stoves-Heating-cooling
/pl/Furnaces-furnace-accessories-Heating-cooling/4294618086
/pl/HVAC-components-Heating-cooling/542366694
/pl/HVAC-duct-fittings-Heating-cooling/4294512241
/pl/Heat-pumps-Heating-cooling/4294618089
/pl/Heating-fuel-tanks-Heating-cooling/4294856699
/c/Humidifiers-dehumidifiers-Heating-cooling
/c/Portable-space-heaters-Heating-cooling
/pl/Radiator-covers-Heating-cooling/4294395587
/c/Registers-grilles-Heating-cooling
/c/Thermostats-Heating-cooling
/c/Christmas-decorations-Holiday-decorations
/pl/Fall-decorations-Holiday-decorations/914756848
/pl/Fourth-of-july-decorations-Holiday-decorations/3007020135
/pl/Halloween-decorations-Holiday-decorations/4294586669
/pl/Hanukkah-decorations-Holiday-decorations/4294586675
/pl/Seasonal-decorations-Holiday-decorations/2850470667
/c/Area-rugs-mats-Home-decor
/c/Bed-bath-Home-decor
/c/Furniture-Home-decor
/c/Home-accents-Home-decor
/pl/Home-decor-collections-Home-decor/2111568621127
/pl/Luggage-travel-Home-decor/255140825
/c/Mirrors-mirror-accessories-Home-decor
/c/Pillows-throws-Home-decor
/c/Wall-art-decor-Home-decor
/c/Wallpaper-accessories-Home-decor
/c/Window-treatments-Home-decor
/pl/Backsplash-panels-Kitchen/4294395588
/c/Kitchen-bar-sinks-Kitchen
/c/Kitchen-cabinetry-Kitchen
/c/Kitchen-countertops-accessories-Kitchen
/c/Kitchen-faucets-water-dispensers-Kitchen
/c/Kitchenware-Kitchen
/c/Garden-decor-Lawn-garden
/c/Garden-hoses-accessories-Lawn-garden
/pl/Greenhouses-accessories-Lawn-garden/4294512248
/c/Insect-pest-control-Lawn-garden
/c/Irrigation-Lawn-garden
/c/Landscaping-Lawn-garden
/c/Lawn-care-Lawn-garden
/c/Outdoor-drainage-Lawn-garden
/c/Pavers-retaining-walls-Lawn-garden
/pl/Plants-planters-Lawn-garden/4294612580
/c/Weed-killers-preventers-Lawn-garden
/c/Bathroom-wall-lighting-Lighting-ceiling-fans
/pl/Ceiling-fan-parts-accessories-Lighting-ceiling-fans/4294395603
/c/Ceiling-fans-Lighting-ceiling-fans
/c/Ceiling-lights-Lighting-ceiling-fans
/c/Commercial-lighting-Lighting-ceiling-fans
/c/Lamps-lamp-shades-Lighting-ceiling-fans
/c/Light-bulbs-Lighting-ceiling-fans
/pl/Lighting-parts-accessories-Lighting-ceiling-fans/4294925669
/pl/Night-lights-Lighting-ceiling-fans/4294857028
/pl/Novelty-lighting-Lighting-ceiling-fans/4294566036
/c/Outdoor-lighting-Lighting-ceiling-fans
/c/Under-cabinet-lighting-Lighting-ceiling-fans
/pl/Brackets-braces-Moulding-millwork/2410111951795
/pl/Dowels-dowel-pins-Moulding-millwork/4294402555
/c/Moulding-Moulding-millwork
/c/Wall-panels-planks-Moulding-millwork
/pl/Bike-accessories-Outdoor-recreation/2321646038739
/pl/Bikes-Outdoor-recreation/2426769188
/pl/Camping-hunting-fishing-Outdoor-recreation/3172089732
/pl/Fireworks-Outdoor-recreation/1820112634192
/pl/Golf-Outdoor-recreation/3515281005
/pl/Metal-detectors-Outdoor-recreation/2321957009384
/pl/RV-accessories-Outdoor-recreation/1403527902
/pl/Recreational-vehicles-Outdoor-recreation/2510965754766
/pl/Scooters-Outdoor-recreation/537872457
/pl/Water-sports-Outdoor-recreation/4294599090
/pl/Winter-sports-Outdoor-recreation/4294610308
/pl/Commercial-park-equipment-Outdoors/4294610286
/c/Fire-pits-patio-heaters-Outdoors
/c/Grills-outdoor-cooking-Outdoors
/pl/Hot-tubs-spas-components-Outdoors/4294610266
/c/Outdoor-games-toys-Outdoors
/c/Outdoor-tools-equipment-Outdoors
/c/Patio-furniture-Outdoors
/c/Playsets-Outdoors
/c/Pools-Outdoors
/c/Sheds-outdoor-storage-Outdoors
/c/Caulking-Paint
/pl/Ceiling-paint-Paint/611625339713
/c/Craft-paint-supplies-Paint
/pl/Door-trim-paint-Paint/861738257
/c/Exterior-paint-Paint
/c/Exterior-stains-floor-coatings-Paint
/c/Interior-paint-Paint
/c/Interior-stains-finishes-Paint
/pl/Paint-cleaners-chemicals-additives-Paint/2521972965619
/c/Paint-samples-Paint
/c/Paint-supplies-Paint
/c/Patching-repair-Paint
/c/Primer-Paint
/c/Specialty-commercial-paint-Paint
/c/Spray-paint-accessories-Paint
/pl/Clippers-trimmers-Personal-care-grooming/4294639586
/pl/Electric-razors-Personal-care-grooming/4294599074
/pl/Hair-styling-tools-Personal-care-grooming/2021690876378
/pl/Health-diagnostic-tools-Personal-care-grooming/2721237196131
/pl/Light-sound-therapy-Personal-care-grooming/1047779848
/pl/Oral-care-Personal-care-grooming/1920577020870
/pl/Shower-radios-Personal-care-grooming/4294639593
/pl/Skin-care-Personal-care-grooming/1542383729
/c/Augers-plungers-drain-openers-Plumbing
/pl/Firestop-products-systems-Plumbing/117408902
/c/Pipe-fittings-Plumbing
/c/Plumbing-parts-repair-Plumbing
/pl/Plumbing-tools-cements-Plumbing/4294607602
/pl/Septic-tanks-accessories-Plumbing/1352416560
/pl/Supply-lines-Plumbing/1149069550
/pl/Tubing-hoses-by-the-foot-Plumbing/2311849919312
/pl/Utility-sinks-faucets-Plumbing/4294639563
/c/Valves-valve-repair-Plumbing
/c/Water-filtration-water-softeners-Plumbing
/pl/Water-heater-parts-accessories-Plumbing/2310003785690
/c/Water-heaters-Plumbing
/c/Water-pumps-tanks-Plumbing
/pl/Child-safety-Safety/4294644944
/pl/Eye-protection-Safety/4294644951
/pl/First-aid-Safety/4294644939
/pl/Hard-hat-accessories-Safety/4294482086
/pl/Hard-hats-Safety/4294644957
/pl/Hearing-protection-Safety/4294644955
/pl/Ice-melt-Safety/4294414320
/pl/Knee-pads-Safety/4294644960
/pl/Marking-flags-Safety/4294559264
/pl/Pepper-spray-Safety/1221059300625
/pl/Protective-clothing-Safety/4294625947
/pl/Respiratory-protection-Safety/721068286897
/pl/Safety-accessories-Safety/4294644945
/pl/Safety-tape-Safety/4294644907
/pl/Safety-vests-Safety/4294644952
/pl/Test-kits-Safety/3385023924
/pl/Traffic-safety-equipment-Safety/4294644940
/pl/Weather-radios-Safety/4294644967
/pl/Home-security-Smart-home-security-wi-fi/2957059063
/pl/Smart-home-Smart-home-security-wi-fi/37721669146452
/pl/Wi-fi-networking-devices-Smart-home-security-wi-fi/2821202638033
/pl/Athletic-field-markers-Sports-fitness/4294515330
/pl/Basketball-systems-Sports-fitness/4294506781
/pl/Bleacher-cushions-seats-Sports-fitness/407195896
/pl/Coolers-water-bottles-Sports-fitness/4294610589
/pl/Fitness-exercise-equipment-Sports-fitness/4294546188
/pl/Sports-equipment-Sports-fitness/2108258635
/c/Baskets-storage-containers-Storage-organization
/c/Closet-organization-Storage-organization
/c/Garage-organization-Storage-organization
/pl/Hooks-racks-Storage-organization/4294936564
/pl/Kitchen-organization-Storage-organization/4294857701
/pl/Laundry-organization-Storage-organization/4294857708
/pl/Lockers-Storage-organization/855642652
/c/Moving-boxes-supplies-Storage-organization
/pl/Office-school-supplies-Storage-organization/2611667535867
/c/Shelves-shelving-Storage-organization
/pl/Small-parts-organizers-Storage-organization/4211758077
/pl/Utility-storage-cabinets-Storage-organization/3721327500
/c/Air-tools-compressors-Tools
/pl/Flashlights-flashlight-bulbs-Tools/2018528687
/c/Hand-tools-Tools
/pl/Jobsite-radios-Tools/195306503
/c/Ladders-scaffolding-Tools
/pl/Levels-measuring-tools-Tools/4294607864
/c/Power-tool-accessories-Tools
/c/Power-tools-Tools
/pl/Shop-vacuums-accessories-Tools/4294857473
/c/Tool-storage-work-benches-Tools
/pl/Walkie-talkies-Tools/1332684016
/c/Welding-soldering-Tools
/pl/Awnings-accessories-Windows-doors/4294858045
/c/Exterior-doors-Windows-doors
/pl/Exterior-shutters-accessories-Windows-doors/4294775790
/c/Garage-doors-openers-Windows-doors
/pl/Hurricane-shutter-panels-Windows-doors/4294858024
/c/Interior-doors-Windows-doors
/pl/Replacement-screens-Windows-doors/2867482404
/pl/Screen-frame-connectors-Windows-doors/2155437395
/pl/Screen-spline-Windows-doors/4294772364
/pl/Screen-tools-Windows-doors/4294772361
/pl/Screening-systems-Windows-doors/555679654
/pl/Weatherstripping-Windows-doors/4294929691
/c/Windows-Windows-doors""".splitlines()

sub_d_links = ["https://www.lowes.com"+i for i in sub_d_links]
print(len(sub_d_links))
# dep_xp = '//*[@aria-label="departments"]/parent::div/div//@href'

class Scraper():
    #Initialising Scraper
    def __init__(self):
        self.robot = '//*[contains(text(),"To proceed, please verify that you are not a robot.")]'
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
    #    options.add_argument("--disable-javascript")
    #    options.add_argument('--headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
        # self.driver = webdriver.Firefox(executable_path="/Users/shubhamyadav/Desktop/amazonCats/geckodriver")
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Remote(
            command_executor=f"https://dev-selenium-grid.katapult.com/wd/hub",
            # desired_capabilities=DesiredCapabilities.CHROME,
            options=options,
        )

    def iterate(self,link):
        self.driver.get(link)
        dep_xp = '//*[@aria-label="departments"]/parent::div/div/ul/li/a'
        sublinks = self.driver.find_elements(By.XPATH,dep_xp)
        sublinks = [i.get_attribute("href") for i in sublinks]
        print(sublinks)
        if len(sublinks) == 0:
            print("sublinks == 0")
            page_source = self.driver.page_source
            # Parse the page source using lxml etree
            tree = etree.HTML(page_source)
            dep_xp = '(//*[@class="GridStyles__GridRow-sc-1ejksnu-1 qwBjG row sc-98d7ri_engage-common-3 jaXDpy"])[1]//@href'
            # sublinks = self.driver.find_elements(By.XPATH,dep_xp)
            sublinks = tree.xpath(dep_xp)
            sublinks = ["https://www.lowes.com"+i for i in sublinks]
        if len(sublinks) > 0:
            for i in sublinks:
                self.iterate(i)
        else:
            with open("lastlinks.txt","a") as fl:
                fl.write(self.driver.current_url)
                fl.write("\n")
                fl.close()


scraper = Scraper()
for i in sub_d_links[:]:
    scraper.iterate(i)
    with open("loop1Last.txt","a") as fl:
        fl.write(i)
        fl.write("\n")
        fl.close()