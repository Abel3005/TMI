import crawling_rocketpunch as cr
import save_json as sj

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    url = 'https://www.rocketpunch.com/api/jobs/template?page={}&job=1'
    
    data_dic = cr.rocketpunch_crawler(url, headers)
    detailed_data = cr.parse_job_page(data_dic, headers)
    sj.save_dataframe(detailed_data)
    
if __name__=="__main__":
    main()