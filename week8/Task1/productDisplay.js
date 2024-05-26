console.time();

function productDisplay() {
    const products = [
        {id: 1, name: '智能手機X1', description: '高效能智能手機，擁有強大攝影功能。', price: 699, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 2, name: '無線耳機Pro', description: '降噪無線耳機，音質清晰。', price: 199, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 3, name: '智慧手錶3', description: '健康監測智慧手錶，續航能力強。', price: 249, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 4, name: '4K電視55寸', description: '超高清4K顯示屏，家庭娛樂最佳選擇。', price: 499, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 5, name: '藍牙音箱', description: '便攜式藍牙音箱，音質卓越。', price: 99, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 6, name: '筆記型電腦', description: '輕薄便攜筆記型電腦，高效處理器。', price: 899, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 7, name: '平板電腦', description: '高性能平板電腦，適合娛樂與工作。', price: 329, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 8, name: '遊戲主機', description: '次世代遊戲主機，遊戲體驗極佳。', price: 499, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 9, name: '智慧家居助手', description: '語音控制智慧家居設備，便利生活。', price: 149, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 10, name: '無人機', description: '高畫質攝影無人機，穩定飛行。', price: 799, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 11, name: '電子書閱讀器', description: '輕便電子書閱讀器，護眼模式。', price: 129, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 12, name: '智能健身手環', description: '多功能健身手環，精確記錄運動數據。', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 13, name: '智能門鎖', description: '高安全性智能門鎖，遠程控制。', price: 199, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 14, name: '車載導航儀', description: '高清車載導航儀，路況實時更新。', price: 249, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 15, name: '咖啡機', description: '快速沖泡和多種咖啡選項', price: 199, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 16, name: '空氣炸鍋', description: '健康烹飪和便捷清洗', price: 149, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 17, name: '電動牙刷', description: '高效清潔和多種模式', price: 79, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 18, name: '無線吸塵器', description: '強大吸力和輕便設計', price: 299, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 19, name: '智能恆溫器', description: '自動調節和節能', price: 199, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 20, name: '智能門鈴', description: '高清視頻和雙向音頻', price: 149, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 21, name: '電子鎖', description: '指紋識別和遠程控制', price: 199, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 22, name: '智能窗簾', description: '遠程控制和定時開關', price: 129, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 23, name: '機械鍵盤', description: '高反應速度和RGB背光', price: 89, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 24, name: '電競滑鼠', description: '高精度和可調DPI', price: 49, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 25, name: '遊戲耳機', description: '環繞音效和降噪麥克風', price: 79, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 26, name: '顯示器', description: '高清分辨率和快速響應時間', price: 299, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 27, name: '外接硬碟', description: '大容量和高速傳輸', price: 109, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 28, name: '無線充電板', description: '快速充電和安全保護', price: 49, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 29, name: '自拍桿', description: '藍牙遙控和便攜設計', price: 19, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 30, name: '運動相機', description: '防水和4K錄影', price: 299, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 31, name: '智能手環', description: '健康追踪和通知提醒', price: 69, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 32, name: '電子秤', description: '精確測量和藍牙同步', price: 39, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 33, name: '水質檢測儀', description: '即時檢測和數據顯示', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 34, name: '藍牙追踪器', description: '防丟失提醒和定位功能', price: 25, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 35, name: '空氣淨化器', description: '高效過濾和靜音設計', price: 199, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 36, name: '加濕器', description: '超聲波技術和多種模式', price: 49, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 37, name: '智能鏡子', description: '顯示時間和天氣預報', price: 129, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 38, name: '洗碗機', description: '高效清洗和節能', price: 499, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 39, name: '果汁機', description: '快速攪拌和易清洗', price: 99, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 40, name: '智能垃圾桶', description: '自動開蓋和密封功能', price: 79, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 41, name: '3D列印機', description: '高精度和多材質打印', price: 599, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 42, name: '電子琴', description: '多種音色和節奏功能', price: 299, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 43, name: '健身器材', description: '多功能和耐用設計', price: 499, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 44, name: '瑜伽墊', description: '防滑和舒適設計', price: 29, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 45, name: '登山包', description: '大容量和耐用材料', price: 79, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 46, name: '睡袋', description: '保暖和便攜', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 47, name: '電動滑板車', description: '長續航和快充', price: 399, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 48, name: '折疊自行車', description: '輕便和便於攜帶', price: 299, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 49, name: '行車記錄儀', description: '高清錄影和夜視功能', price: 149, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 50, name: '車載充電器', description: '快速充電和多接口', price: 29, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 51, name: '車載空氣淨化器', description: '高效過濾和低噪音', price: 79, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 52, name: '汽車導航儀', description: '實時導航和大屏幕顯示', price: 199, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 53, name: '車載冰箱', description: '快速製冷和節能', price: 199, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 54, name: '行李箱', description: '輕便和耐用設計', price: 129, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 55, name: '旅行枕', description: '舒適支撐和便攜', price: 39, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 56, name: '電子翻譯機', description: '多語言支持和快速翻譯', price: 149, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 57, name: '智能眼鏡', description: '增強現實和藍牙功能', price: 199, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 58, name: '智能戒指', description: '健康追踪和通知提醒', price: 99, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 59, name: '睡眠耳機', description: '舒適佩戴和助眠音樂', price: 49, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 60, name: '頸部按摩器', description: '多種按摩模式和便攜', price: 79, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 61, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 62, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 63, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 64, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 65, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 66, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 67, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 68, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 69, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 70, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 71, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 72, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 73, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 74, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 75, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 76, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 77, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 78, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 79, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 80, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 81, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 82, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 83, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 84, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 85, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 86, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 87, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 88, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 89, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 90, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 91, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 92, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 93, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 94, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 95, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 96, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 97, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 98, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 99, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
        {id: 100, name: '肩頸熱敷墊', description: '快速加熱和多檔調節', price: 59, pic: 'https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'},
    ];

    let productsSection = document.getElementById('productsSection');

    products.forEach(function(product) {
        let productDiv = document.createElement('div');

        let productName = document.createElement('h2');
        productName.textContent = product.name;

        let productImg = document.createElement('img');
        productImg.src = product.pic;
        productImg.alt = product.description;

        let productDesc = document.createElement('p');
        productDesc.textContent = product.description;

        let productPrice = document.createElement('p');
        productPrice.textContent = '$ '+product.price;

        let addToCartButton = document.createElement('button');
        addToCartButton.textContent = '添加到購物車';
        addToCartButton.onclick = function(){
            addToCart(product.id);
        };
        
        productDiv.appendChild(productImg);
        productDiv.appendChild(productName);
        productDiv.appendChild(productDesc);
        productDiv.appendChild(productPrice);
        productDiv.appendChild(addToCartButton);
        productsSection.appendChild(productDiv);
    })
};

function addToCart(productId){
    console.log(`商品${productId}已添加到購物車`)
};

document.addEventListener('DOMContentLoaded', productDisplay);

console.timeEnd();