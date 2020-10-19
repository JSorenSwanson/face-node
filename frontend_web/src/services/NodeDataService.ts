// Utilize base url/hostname constants to add DRY 
import http from '@/plugins/http-common';

// Lightweight class which utilizes Axios base def and base url to perform web requests. 
class NodeDataService {
  // return node data service
  getAll() {
    return http.get("/node");
  }
  // return node data by id
  get(nodeid: string) {
    return http.get(`/nodesettings/${nodeid}`);
  }
  // insert/update node data (form data serialized as JSON)
  create(data: any) {
    return http.post("/node/", data);
  }
  
  // return nodes with metadata contained in search field 
  filter(query: string)
  {
    return http.get(`/node/${query}`)
  }

  // update node data
  update(data: any) {
    return http.put("/node/", data);
  }

  // delete node data
  delete(data: any) {
    return http.delete("/node/", data);
  }

  // Some other operations we'll be interested in
  /*
  
  */
}

export default new NodeDataService();