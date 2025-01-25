def getAccountID(String environment){
    switch(environment) { 
        case 'dev': 
            return "983015583980"
        case 'qa':
            return "983015583980"
        case 'uat':
            return "983015583980"
        case 'pre-prod':
            return "983015583980"
        case 'prod':
            return "983015583980"
        default:
            return "nothing"
    } 
}
