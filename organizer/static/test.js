class Body extends React.Component {
    render() {
        return (
            <p>
                Test
            </p>
        );
    }
}

function clickme() {
    ReactDOM.render(
        <Body />,
        document.getElementById('body')
    )
}