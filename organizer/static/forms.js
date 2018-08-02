import { Parser } from 'html-to-react';

//class TextField extends React.Component {
//    render () {
//        return  <div>
//                    <label htmlFor={this.props.name}>{this.props.label}: </label>
//                    <input name={this.props.name} type="text"/><br/>
//                </div>;
//    }
//}

//class MyForm extends React.Component {
//    render() {
//        let components = (JSON.parse(window.context))['log_in'];
//        let xml = components.map(function (element, i) {
//            element['key'] = i;
//            if (element['type'] === 'text') {
//                return React.createElement(
//                    TextField,
//                    element
//                )
//            }
//            else {
//                alert('non-text not implemented');
//            }
//        });
//        return (
//            <form method="post">
//                {xml} <input type="submit" value="Go"/>
//            </form>
//        );
//    }
//}

let htmlToReactParser = new Parser();
let reactElement = htmlToReactParser.parse(window.context);

ReactDOM.render(
    reactElement,
    document.getElementById('body')
);