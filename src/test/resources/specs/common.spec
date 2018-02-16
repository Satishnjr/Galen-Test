
@objects
    header-img.responsive     css      img[class='img-responsive'] 
    header-div.row            xpath    //*[@id="header"]/div[2]/div/div
    header-logo               css      img[class='logo img-responsive']
    search_box                id       search_query_top
    


= Header =
    @on *
    	header-img.responsive:
			inside screen 0px top
			centered horizontally inside screen 1px
			
            
		header-div.row:
			height ~ 38px
			inside header-div.row 0px top
			centered horizontally inside screen 1px
		
        
            
            
    @on desktop
    	header-img.responsive:
    		width 1170px 
    		height 65px
    		
		header-logo:
			below header-div.row ~ 15px
			width < 351px                                                                           
			height < 101px
			css font-family is  "Arial, Helvetica, sans-serif"
			css font-size is "13px" 
			
		header-div.row:
			width 1170px
			
			 
		search_box:
			below header-div.row 50px
			width < 371px                                                                           
			height ~ 45px
			
			
	@on mobile
		header-img.responsive:	
			width 387px 
			height 22px
			
		header-div.row:
			width 387px
			
		header-logo:
			below header-div.row ~ 15px
			width 350px                                                                           
			height < 101px
			css font-family is  "Arial, Helvetica, sans-serif"
			css font-size is "13px" 
			
			 
		search_box:
			below header-div.row 164px
			width < 390px                                                                           
			height ~ 45px
			
	@on tablet
		header-img.responsive:
			width 687px
			height 38px
			
		header-div.row:
			width 687px  
			
		header-logo:
			below header-div.row ~ 15px		
			width  350px 						                                                                         
			height < 101px
			css font-family is  "Arial, Helvetica, sans-serif"
			css font-size is "13px" 
			
			 
		search_box:
			below header-div.row 164px
			#width > 687px                                                                           
			height ~ 45px
     
		