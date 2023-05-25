package study;

import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.List;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;


 
public class macro {
	
    public static void main(String[] args) throws URISyntaxException, InterruptedException, IOException {
        /*
            Document 클래스 : 연결해서 얻어온 HTML 전체 문서
            Element 클래스  : Documnet의 HTML 요소
            Elements 클래스 : Element가 모인 자료형
        */       
    	
        System.setProperty("webdriver.chrome.driver", "D:\\chromedriver_win32\\chromedriver.exe");
        
      
        
		  // WebDriver 인스턴스 생성
        //WebDriver driver = new ChromeDriver();
		WebDriver driver;
        
        
   
        //String url = "https://booking.naver.com/booking/3/bizes/2066/items/4728225?startDate=2023-06-28&endDate=2023-06-30";

        String url = "https://www.naver.com/";
        String user_id = "leejc831";
        String user_pw = "qrg258*01";
        

        //Runtime.getRuntime().exec("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir=\"D:\"");
        ChromeOptions options = new ChromeOptions();
      	options.addArguments("--start-maximized");
      	options.addArguments("--disable-popup-blocking");
        //options.setExperimentalOption("debuggerAddress", "127.0.0.1:9222");
        driver = new ChromeDriver(options); 
		Thread.sleep(1000); // 3. 페이지 로딩 대기 시간
        driver.get(url);
        

        WebElement element;
     // 1. 로그인 버튼 클릭
		element = driver.findElement(By.className("MyView-module__link_login___HpHMW"));
 		element.click();
 		Thread.sleep(1000);
  
 		
 	// ID 입력
		element = driver.findElement(By.id("id"));
		element.sendKeys("leejc831");
		element.sendKeys(Keys.CONTROL, "v");
		
	
 				
		// 비밀번호 입력
		element = driver.findElement(By.id("pw"));
		element.sendKeys("qrg258*01");
		
		// 전송
		element = driver.findElement(By.className("btn_login"));
		element.submit();

    
    }
    
}
  