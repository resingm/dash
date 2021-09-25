import { A } from '@ember/array';
import Component from '@glimmer/component';
import { inject as service } from '@ember/service';
import { tracked } from '@glimmer/tracking';

export default class NavbarComponent extends Component {
  @service('state') state;

  /*
  get lastUpdate() {
    console.log("lastUpdate");
    console.log(this.state.lastUpdate);
    //return this.state.lastUpdate;
    return "placeholder";
  }
  */
}
