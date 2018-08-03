import { Parser } from 'html-to-react';

class FormRaw extends React.Component {
    constructor(props) {
        super(props);

        let htmlToReactParser = new Parser();
        let Comp = htmlToReactParser.parse(window.context[this.props.name]);

        this.Comp = Comp;
    }
    
    render() {
        let children = this.Comp.props.children.map(this.props.componentParser);
        return (<div>{children}</div>);
    }
}

export class FormBody extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
        this.processPOST = this.processPOST.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.processChild = this.processChild.bind(this);
        //this.onLoad = this.onLoad.bind(this);
    }
    
    static onLoad() {
        console.log('Recieved load')
    }
    
    processPOST() {
        let http = new XMLHttpRequest();
        http.open('POST', '/', true);
        
        // Create message
        let message = 'name=' + this.props.name;
        for (let key in this.state) {
            message +=  '&' + key + '=' + this.state[key]
        }
        
        http.onload = FormBody.onLoad;
        http.send(message);
    }
    
    handleChange(event) {
        let obj = {};
        obj[event.target.name] = event.target.value;
        this.setState(obj);
    }
    
    processChild(element) {
        if (element.type === 'input') {
            if (!this.state.hasOwnProperty(element.props.name)){
                this.state[element.props.name] = '';
            }
            
            return (<input
                {...element.props}
                value={this.state[element.props.name]}
                onChange={this.handleChange}
            />)
        } else {
            return element;
        }
    }
    
    render() {
        return (
            <form method="post">
                <FormRaw name={this.props.name} componentParser={this.processChild}/>
                <button onClick={this.processPOST}>
                    Sign In
                </button>
            </form>
        );
    }
}