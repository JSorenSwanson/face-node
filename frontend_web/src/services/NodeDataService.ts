// Utilize base url/hostname constants to add DRY 
import http from '@/plugins/http-common';

// Lightweight class which utilizes Axios base def and base url to perform web requests. 
class NodeDataService {
  // return node data service
  getAll() {
    return http.get("/node");
  }
  // return node data by id
  get(nodeid: string, jwt: any) {
    return http.get(`/nodesettings/${nodeid}`,{ headers: { Authorization: `Bearer: ${jwt}` } });
  }
  // insert/update node data (form data serialized as JSON)
  create(data: any, jwt: any) {

  /* 
      Would likely be better practice to implement an object mapper for translating
      attributes of flat JSON data objects.
  */

    const payload = {
      nodeAttributes:{
        name:data.name, 
        description:data.description,
        location:data.location
      },
      nodeSettings:{
        resolution: data.res,
        ip: data.ip, 
        fps: data.fps,
        confidence: data.confidence
      }
    }

    return http.post(
      "/node/", 
      payload, 
      { 
        headers: 
        { 
          Authorization: `Bearer: ${jwt}` 
        } 
      });
  }
  
  // return nodes with metadata contained in search field 
  filter(query: string)
  {
    return http.get(`/node/${query}`)
  }

  // Some other operations we'll be interested in
  /*
  update

  delete

  */
}

export default new NodeDataService();