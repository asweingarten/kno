/// <reference path="../typings/react/react.d.ts" />
/// <reference path="../typings/jquery/jquery.d.ts" />
import React = __React;


// React Views
interface HeadlineProps extends React.Props<any> {
  text: string;
}

interface HeadlinesProps extends React.Props<any> {
  headlines: string[];
}

class Headline extends React.Component<HeadlineProps, {}> {
  render() {
    return <li>{this.props.text}</li>;
  }
}

class Headlines extends React.Component<HeadlinesProps, {}> {
  render() {
    var headlines = this.props.headlines;
    var headlineElements = headlines.map(function(headline) {
      return (<Headline text={headline} />);
    }, this);
    
    return (
      <ul>
        {headlineElements}
      </ul>
    );
  }
}

// Application Logic
let apiEndpoint:string = "http://kno.ccl.io:6001/top?prefetch=true&term=";

var headlines:string[] = ['hello', 'tomato'];
var content:any;

$(() => {
    let target = document.getElementById('container');
  
    $.get(apiEndpoint, { term: 'Apple' }, (rawArticles:string) => {
      // console.log(articles);
      let articles:any[] = JSON.parse(rawArticles);
      headlines = $.map(articles, function(article) {
        return article.title;
      });
      
      console.log(headlines);
      content = <Headlines headlines={headlines} />;
      React.render(content,target);
    });
    
});