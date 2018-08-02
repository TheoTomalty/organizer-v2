import { Parser } from 'html-to-react';

export class LoginInterface {
    render() {
        let htmlToReactParser = new Parser();
        let reactElement = htmlToReactParser.parse(window.context['sign_up']);
        
        ReactDOM.render(
            reactElement,
            document.getElementById('body')
        );
    };
}

let login_interface = new LoginInterface();
login_interface.render();