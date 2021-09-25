import { A } from '@ember/array';
import Component from '@glimmer/component';
import { inject as service } from '@ember/service';
import { tracked } from '@glimmer/tracking';

export default class DashboardComponent extends Component {
  @service('state') state;
  @tracked items = A([]);

  interval = 2000;
  refresher = null;

  constructor(owner, args) {
    super(owner, args);

    // this.refresh();
    this.start();
  }

  willDestroy() {
    super.willDestroy(...arguments);
    this.shutdown();
  }

  async start() {
    //this.refresher = setInterval(await this.refresh(), this.interval);
    this.refresher = setInterval(async () => {
      await this.refresh();
    }, this.interval);
  }

  async shutdown() {
    if (!this.refresher) {
      // If interval is not set, leave
      return;
    }

    clearInterval(this.refresher);
  }

  async refresh() {
    await this.state.refresh();
    this.items = this.state.get();
  }
}
