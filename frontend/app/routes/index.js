import Route from '@ember/routing/route';

export default class IndexRoute extends Route {
  async model() {
    return {
      data: [
        {
          type: 'card',
          id: '1',
          attributes: {
            purpose: 'demonstration',
            comment: 'This card provides some demo data.',
          },
          meta: {
            title: 'Demo View',
            subtitle: 'Just shows a card.',
          },
        },
        {
          type: 'card',
          id: '2',
          attributes: {
            attribute_name: 'Attribute Name',
            small_number: 1,
            large_number: 157105,
            decimal: 3.14159,
            uuid: '1bba5efb-cd7d-41b9-a86b-a3bac6907098',
          },
          meta: {
            title: 'Values',
          },
        },
        {
          type: 'card',
          id: '1',
          attributes: {
            latitude: 52.2209,
            longitude: 6.8953,
            temperature: 24.7,
            temperate_feeling: 24.98,
            clouds: 100,
            wind: 1.34,
          },
          meta: {
            title: 'Weather Enschede',
          },
        },
      ],
    };
  }
}
