import results_processor
import db_module


def run(args):
    print('Loading CLI')
    print(args.get)
    if args.get:
        site_data = results_processor.process_url(args.get)
        is_save = input('\nWould you like to save results? (Y/N)')
        if is_save is 'Y':
            site_name = input('Please enter site name:')
            db_module.save_results(site_name, site_data.base_url, site_data.datetime_stamp, site_data.tags_dict)
        else:
            print('As you wish. Bye!')
    elif args.view:
        results_processor.show_results(args.view)




