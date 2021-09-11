import Component from '@ember/component';
import { tracked } from '@glimmer/tracking';
import { action } from '@ember/object';
import { A } from '@ember/array';

export default class DashboardComponent extends Component {
  @tracked items = A([])

  init() {
    super.init(...arguments);

    this.empty();

    //const res = fetch("http://localhost/api");
    //
    fetch("http://localhost/api").then((res) => {
      if (!res.ok) {
        console.log("Error");
      }
      return res.json();
    }).then((res) => {
      res.data.forEach(x => this.add(x));
    });
  }

  add(item) {
    this.items.pushObject(item);
  }

  remove(item) {
    this.items.removeObject(item);
  }

  empty() {
    this.items.clear();
  }
}

import Route from '@ember/routing/route';

