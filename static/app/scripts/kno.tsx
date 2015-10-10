/// <reference path="../typings/react/react.d.ts" />
/// <reference path="../typings/jquery/jquery.d.ts" />
import React = __React;

interface Article {
  title: string;
  id: string;
  entities: string[];
  image: any;
  url: string;
  text: string;
}

// React Views
interface HeadlineProps extends React.Props<any> {
  title: string;
  id: string;
}

interface HeadlinesProps extends React.Props<any> {
  articles: Article[];
}

class Headline extends React.Component<HeadlineProps, {}> {
  render() {
    let link = 'http://kno.ccl.io:6001/static/wav/' + this.props.id + '.wav';
    return <li><a href={link}> {this.props.title}</a></li>;
  }
}

class Headlines extends React.Component<HeadlinesProps, {}> {
  render() {
    var articles = this.props.articles;
    var headlineElements = articles.map(function(article) {
      return (<Headline title={article.title} id={article.id} />);
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
      let articles:Article[] = JSON.parse(rawArticles);
      // headlines = $.map(articles, function(article) {
      //   return {
      //     title: article.title,
      //     id: article.id
      // });
      
      console.log(articles);
      content = <Headlines articles={articles} />;
      React.render(content,target);
    });
    
});