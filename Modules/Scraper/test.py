
import bal_excel_scraper as Scraper

dir = "../../test.xlsx"

def main() :
    
    sheet = Scraper.bal_load_excel(dir)

    routine_name = Scraper.bal_get_routine_name(sheet)
    author = Scraper.bal_get_author(sheet)
    training_num = Scraper.bal_get_training_per_weeks(sheet)
    weight_unit = Scraper.bal_get_weight_unit(sheet)
    lifting_category = Scraper.bal_get_lifting_category(sheet)
    lifting_set = Scraper.bal_get_lifting_set(sheet,0)
    ae = Scraper.bal_get_assistance_exercise(sheet,0)


    print(routine_name)
    print(author)
    print(training_num)
    print(weight_unit)
    print(lifting_category)
    print(lifting_set)
    print(ae)

if __name__ == "__main__" :
    main()