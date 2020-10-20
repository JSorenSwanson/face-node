// Utilize base url/hostname constants to add DRY 
import http from '@/plugins/http-common';

// Lightweight class which utilizes Axios base def and base url to perform web requests. 
class UserDataService {
    // Register new user
    // insert/update node data (form data serialized as JSON)
    create(data: any) {
        return http.post("/user/", data);
    }
    // Attempt to validate user creds, retrieve JWT token for storage
    login(data: any) {
        return http.post("/user/login", data);
    }
}

export default new UserDataService();