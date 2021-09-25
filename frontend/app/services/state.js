import { A } from '@ember/array';
import Service from '@ember/service';
import { tracked } from '@glimmer/tracking';

export default class IndexService extends Service {
  items = A([]);
  @tracked lastUpdate;

  add(item) {
    this.items.pushObject(item);
  }

  clear() {
    this.items.clear();
  }

  get() {
    return this.items;
  }

  async refresh() {
    let res = await fetch('http://localhost/api/');
    this.lastUpdate = new Date(Date.now()).toUTCString();

    if (res.ok) {
      let q = await res.json();
      this.clear();
      q.data.forEach((x) => this.add(x));
    } else {
      let err = {
        type: 'card',
        id: '1',
        attributes: {
          status: res.status.toString(),
          statusText: res.statusTest,
          ok: res.ok.toString(),
          type: res.type.toString(),
          url: res.url.toString(),
        },
        meta: {
          title: `${res.status} - ${res.statusText}`,
          subtitle: 'Error details',
        },
      };

      this.clear();
      this.add(err);
    }
  }
}
