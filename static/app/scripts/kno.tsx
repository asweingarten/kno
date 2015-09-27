/// <reference path="../typings/react/react.d.ts" />
/// <reference path="../typings/react/react.d.ts" />
import React = __React;

interface HelloWorldProps extends React.Props<any> {
  name: string;
}

class Hello extends React.Component<HelloWorldProps, {}> {
  render() {
    return <div>Hello {this.props.name}</div>;
  }
}

let content = <Hello name="Ariel" />

$(() => {
    let target = document.getElementById('container');
    React.render(content,target);
});

// React.render(content, document.getElementById('container'));