export interface INode{
    id?: number;
    description: string; 
    name: string; 
    location: string; 
}
export class NodeDTO implements INode{
    id?: number; 
    description: string = '';
    name: string = ''; 
    location: string = ''; 
}
export default class Node extends NodeDTO{
    constructor(dto: NodeDTO)
    {
        super();
        Object.assign(this, dto)
    }
}